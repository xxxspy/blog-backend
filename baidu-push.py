import requests
import os
from pathlib import Path
import datetime

here = Path(os.path.dirname(os.path.abspath(__file__)))
mysite = 'http://www.mlln.cn'
# tmp_file = here / '_tmp_urls'
public = here / 'public'


def _push_page(type, pages):
    token = os.getenv('XIONGZHANGHAO_TOKEN')
    url = f'http://data.zz.baidu.com/urls?appid=1600845001263316&token={token}&type={type}'
    pages = [f'{mysite}/{p}' for p in pages]
    print(pages)
    pages = '\n'.join(pages)
    pages = pages.encode('utf8')
    r = requests.post(url,
                      headers={'User-Agent': 'curl/7.12.1'},
                      files={
                          'file': pages
                      })
    print('推送结果:', r.json())


def push(action='today', newest_num=1, type='realtime'):
    assert type in ('realtime', 'batch')
    assert action in ('newest', 'today')
    now = datetime.datetime.now()
    if action == 'today':
        dirpath = now.strftime("%Y/%m/%d")
        post_dir = public / dirpath
        if post_dir.exists():
            pages = []
            f: Path
            for f in post_dir.iterdir():
                if f.is_dir():
                    pages.append(f'{dirpath}/{f.name}')
            _push_page(type, pages)
            return
    pages = []
    for y in range(now.year, 2010, -1):
        for m in range(12, 0, -1):
            for d in range(31, 0, -1):
                y = str(y)
                m = str(m)
                d = str(d)
                if len(m) == 1:
                    m = '0' + m
                if len(d) == 1:
                    d = '0' + d
                dirpath = f'{y}/{m}/{d}'
                post_dir = public / dirpath
                if post_dir.exists():
                    for f in post_dir.iterdir():
                        if f.is_dir():
                            pages.append(f'{dirpath}/{f.name}')
                        if len(pages) >= newest_num:
                            _push_page(type, pages)
                            return


if __name__ == '__main__':
    push(action='newest', newest_num=40, type='batch')
