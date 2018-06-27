from selenium import webdriver
import pickle
from pathlib import Path
import os
import uuid
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import os
import yaml

driver_path = 'geckodriver.exe'
here = Path(__file__).parent.absolute()
comment_dir = here / 'source' / 'comments'
img_dir = comment_dir / 'images'
data_path = here / 'source' / '_data' / 'comments.json'
config_path = here / '_config.yml'
browser = webdriver.Firefox(executable_path=driver_path)
login_url = 'http://changyan.kuaizhan.com/'
browser.get(login_url)


def get_login_info():
    e = os.getenv('CHANGYAN_EMAIL')
    p = os.getenv('CHANGYAN_PWD')
    return e, p


def login(browser: webdriver.Firefox, email, password):
    email_input = browser.find_element_by_id('email')
    pwd_input = browser.find_element_by_id('password')
    email_input.send_keys(email)
    # 验证码
    code = input('请输入验证码')
    code_input = browser.find_element_by_id('vcode')
    login_btn = browser.find_element_by_id('login-btn')
    pwd_input.click()
    pwd_input.send_keys(password)
    time.sleep(0.1)
    code_input.click()
    code_input.send_keys(code)
    code_input.send_keys(Keys.ENTER)
    time.sleep(1)


def parse_comments(table):
    trs = table.find_elements_by_tag_name('tr')
    comments = []
    for tr in trs:
        comment = {}
        a = tr.find_element_by_class_name('topic-title')
        comment['title'] = a.text
        comment['href'] = a.get_attribute('href')
        if comment['href'] == '':
            break
        infos = tr.find_element_by_class_name('cmt-info')
        ps = infos.find_elements_by_tag_name('p')
        comment['name'] = ps[0].text
        comment['id'] = ps[1].text
        comment['ip'] = ps[2].text
        comment['date'] = ps[3].text
        comment['content'] = tr.find_element_by_class_name('cmt-content').text
        comment = clean_comment(comment)
        img_path = img_dir / (comment['id'] + '.png')
        if not img_path.exists():
            img = tr.find_element_by_tag_name(
                'img').screenshot_as_png
            with open(img_path, 'wb') as f:
                f.write(img)

        comments.append(comment)
    return comments


def clean_comment(comment: dict,
                  id_format=re.compile('\d+'),
                  ip_format=re.compile('[0-9\.]+'),
                  url='http://mlln.cn/',
                  title_suffix=' - DataScience'):
    '''清理信息'''
    comment['id'] = id_format.findall(comment['id'])[0]
    comment['ip'] = ip_format.findall(comment['ip'])[0]
    comment['href'] = comment['href'].strip(url)
    comment['title'] = comment['title'].strip(title_suffix)
    return comment


def download(browser: webdriver.Firefox):
    # li = browser.find_element_by_class_name('comment-audit-li')
    # li.click()
    # time.sleep(1)
    browser.get('http://changyan.kuaizhan.com/audit/comments/TOAUDIT/1')
    time.sleep(0.5)
    nav = browser.find_element_by_class_name('second-nav')
    nav.find_elements_by_tag_name('li')[1].click()
    time.sleep(0.2)
    rtn = []
    while True:
        table = browser.find_element_by_class_name('table')
        comments = parse_comments(table)
        rtn.extend(comments)
        next_a = browser.find_element_by_link_text('下一页')
        if next_a.find_element_by_xpath('..').get_attribute('class') == 'disabled':
            break
    # 按照时间顺序排序
    rtn.sort(key=lambda x: x['date'], reverse=True)
    data = json.dumps(rtn)
    data_path.write_text(data, encoding='utf8')
    return rtn


def page_content(page, title='最新评论', type='comments'):
    r = (f'---\n'
         f'title: {title}\n'
         f'type: {type}\n'
         f'page: {page}\n'
         f'---\n')
    return r


def generate_page(comments):
    from math import ceil
    with open(config_path, 'r', encoding='utf8') as stream:
        config = yaml.load(stream)
    per_page = int(config['comment_per_page'])
    N = len(comments)
    n_page = ceil(N / per_page)
    for i in range(n_page):
        fname = f'index.{i}.md.'
        content = page_content(i)
        fpath = comment_dir / fname
        fpath.write_text(content, encoding='utf8')
        print(f'Writing to {fpath}')
    # 默认首页
    fname = 'index.md'
    content = page_content(0)
    fpath = comment_dir / fname
    fpath.write_text(content, encoding='utf8')
    print(f'Writing to {fpath}')



if __name__ == '__main__':
    email, password = get_login_info()
    login(browser, email, password)
    comments = download(browser)
    generate_page(comments)
