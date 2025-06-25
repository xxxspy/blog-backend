from crawl4ai import AsyncWebCrawler
from pathlib import Path 
import asyncio
import base64
import json
import requests
import hashlib
from litellm import completion
import dotenv
import re
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from joblib import Memory
from datetime import datetime
import shutil
from urllib.parse import urljoin, urlparse

memory = Memory('.cache')

HERE = Path(__file__).parent
SOURCE_DIR = HERE.parent / 'source/_posts'

dotenv.load_dotenv(HERE.parent/'.envs')
CrawResultFileName = 'crawl-result.json'

def str_compress(long_string : str, length=20)->str:
    """压缩字符串"""
    # 使用 MD5 哈希函数
    hash_object = hashlib.md5(long_string.encode('utf8'))
    # 获取哈希值的十六进制表示
    hex_dig = hash_object.hexdigest()
    # 截取前20个字符
    compressed_string = hex_dig[:length]
    return compressed_string


def extract_urls(mdcontent: str):
    '''从markdown内容中提取链接网址urls，包括绝对和相对（/开头和非/开头）链接'''
    # 匹配 Markdown 链接、裸露的 URL、以 / 开头的相对链接和非/开头的相对链接
    url_pattern = re.compile(
        r'\[.*?\]\((https?://[^\s)]+|/[^\s)]+|[^\s)/]+)\)',  # [text](http(s)://...) 或 [text](/...) 或 [text](相对路径)
        re.IGNORECASE
    )
    urls = []
    for match in url_pattern.finditer(mdcontent):
        # 优先 group(1)（即 markdown 链接），否则取整个匹配
        url = match.group(1) if match.group(1) else match.group(0)
        urls.append(url)
    return urls

# @memory.cache
async def web2markdown(url, output_dir: Path, outfname: str='page.md', redownload=False)->dict:
    """Fetch web page and convert to markdown using crawl4ai

    Args:
        url (_type_): page url
        output_dir (Path): output directory
        outfname (str): _description_
        redownload (bool, optional): rewrite downloaded files. Defaults to False.

    Returns:
        dict: {'mdfile': Path, 'medias': list[Path]}
    """
    output_dir.mkdir(exist_ok=True, parents=True)
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url, screenshot=True)
        print('url:', url, result.status_code)
        if result.screenshot:
            ssfpath = output_dir / 'screenshot.png'
            print('ssfpath', ssfpath)
            ssfpath.write_bytes(base64.b64decode(result.screenshot))
        outfpath = output_dir / outfname
        markdown = result.markdown
        urls = extract_urls(markdown)
        resdata = {
            'images': result.media.get('images', []),
            'videos': result.media.get('videos', []),
        }
        resultpath = output_dir / CrawResultFileName
        resultpath.write_text(json.dumps(resdata, ensure_ascii=False), encoding='utf8')
        medias = []
        mediadir = output_dir / 'medias'
        mediadir.mkdir(exist_ok=True)
        for img in resdata['images'] + resdata['videos']:
            src = img['src']
            # download image from url
            # turn relative url to absolute url
            if src.startswith('http'):
                absurl = src
            else:
                absurl = url.strip('/') + '/' + src.strip('/')
            suffix = src.split('.')[-1].split('?')[0]
            shortname = str_compress(src)
            imgpath = mediadir / f'{shortname}.{suffix}'
            medias.append(imgpath)
            if imgpath.exists() and not redownload: continue
            data = requests.get(absurl).content
            imgpath.parent.mkdir(parents=True, exist_ok=True)
            imgpath.write_bytes(data)
            
        
            markdown = markdown.replace(src, f'medias/{shortname}.{suffix}')
    outfpath.write_text(markdown, encoding='utf-8')
    print(urls)
    return [outfpath, medias, urls]
            
# @memory.cache
def sync_web2markdown(url, output_dir: Path, outfname: str='page.md', redownload=False)->dict:
    """Fetch web page and convert to markdown using crawl4ai

    Args:
        url (_type_): page url
        output_dir (Path): output directory
        outfname (str): _description_
        redownload (bool, optional): rewrite downloaded files. Defaults to False.

    Returns:
        dict: {'mdfile': Path, 'medias': list[Path]}
    """
    return asyncio.run(web2markdown(url, output_dir, outfname, redownload))



# sync_web2markdown('https://www.spss-tutorials.com/basics/', 'manager/.outputs/test')

class ResourceUrl:
    filedirname = '_files_'

    def __init__(self, url: str, output_dir: Path, file_exts: list):
        self.output_dir = output_dir
        self.url = url
        self.file_exts = file_exts
    
    def is_file(self) -> bool:
        '''判断url是否是一个文件, 比如图片或者excel数据或者.sav文件等等'''
        # 常见文件扩展名
        file_exts = self.file_exts
        return any(self.url.lower().split('?')[0].endswith(ext) for ext in file_exts)
    
    def file_path(self)->Path:
        file_dir = self.output_dir / self.filedirname
        file_dir.mkdir(parents=True, exist_ok=True)
        return file_dir / self.filename()
    
    def download_file(self):
        file_path = self.file_path()
        if not file_path.exists():
            try:
                resp = requests.get(self.url)
                if resp.status_code == 200:
                    file_path.write_bytes(resp.content)
                    print(f'Downloaded image: {self.url} -> {file_path}')
            except Exception as e:
                print(f'Failed to download image: {self.url}, error: {e}')

    def filename(self)->str:
        url = self.url
        return self.url_path().replace('/', '-').strip('.') + '.' + url.split('.')[-1].split('?')[0]


    def relative_file_path(self)->str:
        return f'{self.filedirname}/{self.filename()}'
    
    
    def url_path(self)->str:
        url = self.url
        parsed = urlparse(url)
        # 去除开头的斜杠，避免Path把它当作绝对路径
        url_path = parsed.path.lstrip('/')
        # 去除结尾的斜杠
        url_path = url_path.rstrip('/')
        return url_path
    
    def page_output_dir(self)->Path:
        # 拼接输出目录
        return self.flatten_path()

    def flatten_path(self)->Path:
        return self.output_dir / self.dirname()
    
    def dirname(self)->str:
        return self.url_path().replace('/', '-').strip('.')



def download_whole_site(start_url: str, base_url: str, output_dir: Path, ignore_urls=[], file_exts=[]):
    '''下载整个网站
    start_url: 开始页
    base_url: 主域名. 例如 https://www.spss-tutorials.com
    output_dir: 保存文件夹目录
    '''
    output_dir.mkdir(exist_ok=True, parents=True)
    visited = set()
    to_visit = [start_url]
    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        # 判断是否为图片链接
        reurl = ResourceUrl(url, output_dir)
        if reurl.is_file():
            # 下载图片到 output_dir/_files_
            file_path = reurl.file_path()
            if not file_path.exists():
                reurl.download_file()
            visited.add(url)
            continue
        visited.add(url)
        print(f'Downloading: {url}')
        # 生成与url路径对应的本地目录结构
        pagemd = reurl.page_output_dir() / 'page.md'
        if pagemd.exists():
            urls = extract_urls(pagemd.read_text('utf8'))
        else:
            mdfile, medias, urls = sync_web2markdown(url, reurl.page_output_dir())
        for link in urls:
            if any(iu in link or re.search(iu, link) for iu in ignore_urls):
                continue
            if link.startswith('#'): # 页内链接
                continue
            elif link.startswith('http'):
                if link.startswith(base_url):
                    if link not in visited and link not in to_visit:
                        to_visit.append(link)
            elif link.startswith('/'):
                abs_url = urljoin(base_url, link)
                if abs_url not in visited and abs_url not in to_visit:
                    to_visit.append(abs_url)
            else:
                # 相对路径
                abs_url = urljoin(url, link)
                if abs_url.startswith(base_url) and abs_url not in visited and abs_url not in to_visit:
                    to_visit.append(abs_url)

DOWNLOAD_DIR = HERE/'.outputs/spss-tutorials'
OUTPUT_DIR = HERE.parent / 'source/_posts/000 SPSS/00 SPSS入门教程'

file_exts =  (
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp',
            '.xls', '.xlsx', '.csv', '.tsv', '.sav', '.zip', '.rar',
            '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.txt', '.json',
            '.xml', '.tar', '.gz', '.7z', '.mp4', '.mp3', '.avi', '.mov',
            '.sps', '.spe', '.html', '.sgt'
        )

@memory.cache
def make_tutorial(mdcontent: str):
    prompt = f'''# 任务
- 根据原文章翻译或者撰写为一篇中文文章
- 生成符合中文阅读习惯的教程
- 如果是专业术语/软件界面文字或其他关键词, 你需要保留中文和英文, 方便读者理解
- 不要更改链接

# 原文

<!-- 原文开始 -->
{mdcontent}
<!-- 原文结束 -->

# 输出

仅输出中文文章教程, 不要输出其他任何语言, 不要输出客套语
'''
    response = completion(
        model="gemini/gemini-2.0-flash", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

@memory.cache
def remove_urls(content: str):
    prompt = f'''# 任务
- 我不希望文章中包含带有域名网站的链接
- 请删除带有域名的网页链接/并修改内容为合理的格式
- 保留相对路径的链接
- 但是要保留图片和视频链接

# 原文

<!-- 原文开始 -->
{content}
<!-- 原文结束 -->

# 输出

仅输出中文文章教程, 不要输出其他任何语言, 不要输出客套语
'''
    response = completion(
        model="gemini/gemini-2.0-flash", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


def _download_img(imgurl: str, mediadir: Path)->Path:
    '''下载图片, 保存到mediadir, 图片文件名使用imgurl文件名, 返回新的路径'''
    imgname = imgurl.split('/')[-1].split('?')[0]
    imgpath = mediadir / imgname
    if not imgpath.exists():
        mediadir.mkdir(parents=True, exist_ok=True)
        resp = requests.get(imgurl)
        resp.raise_for_status()
        img_bytes = resp.content
        imgpath.write_bytes(img_bytes)
    return imgpath


def make_blog(mdcontent: str)->str:
    # 生成指定日期字符串
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = get_title(mdcontent)
    return f'''---
title: {title}
date: {date_str}
---

{mdcontent}
'''

def media_url_to_absolute(md, datepath, relative_to_posts, dirname):
    """
    从markdown内容中查找所有图片链接，返回所有链接列表。
    例如: ![alt](medias/da7a29326ad492832ce5.png) -> medias/da7a29326ad492832ce5.png
    """
    pattern = re.compile(r'!\[.*?\]\((medias/[^)]+)\)')
    urls = pattern.findall(md)
    for url in urls:
        print(url)
        topath = f'{datepath}/{relative_to_posts}/{dirname}/{url}'.replace('\\', '/').replace(' ', '%20')
        md = md.replace(url, topath)
    return md


@memory.cache
def get_title(content: str) -> str:
    '''使用大语言生成文章标题'''
    prompt = f'''# 任务
- 根据原文内容生成一个简洁、准确的中文标题
- 不要包含多余修饰词或客套语

# 原文

<!-- 原文开始 -->
{content}
<!-- 原文结束 -->

# 输出

仅输出标题，不要输出其他内容
'''
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()


def translate_md(src_dir: Path, output: Path, 
                 base_url: str, ignore_name_ptns=[], 
                 ignore_contents=[], file_exts=[], max_n=-1):
    output.mkdir(exist_ok=True, parents=True)
    # base_path = output.relative_to()
    relative_to_posts = output.relative_to(SOURCE_DIR)
    trans_count = 0
    # copy _files_
    srcfiles = src_dir / '_files_'
    if srcfiles.exists():
        tofiles =  output/'_files_'
        if tofiles.exists():
            shutil.rmtree(tofiles)
        shutil.copytree(srcfiles,tofiles)
    
    for dir in src_dir.iterdir():
        if not 'association-between-metric-and-dichotomous-variable' in dir.name:
            continue
        mdfile = dir / 'page.md'
        if not mdfile.exists():
            continue
        if any(inp in dir.name for inp in ignore_name_ptns):
            continue
        md = mdfile.read_text('utf8')
        if any(ic in md for ic in ignore_contents):
            continue
        print('\n\n\nTranslate file:', mdfile)
        datepath = datetime.now().strftime("%Y/%m/%d")

        print('spss-population-pyramid-unstyled:', 'spss-population-pyramid-unstyled' in md)
        print('extract_urls(md)::::::::', extract_urls(md))
        for url in extract_urls(md):
            print('url ext:', url)
            reurl = ResourceUrl(url, src_dir, file_exts)
            if reurl.is_file():
                if not reurl.file_path().exists():
                    print('download:', url)
                    reurl.download_file()
                else:
                    print('exist:', reurl.file_path())
                tofilepath = reurl.relative_file_path()
                tofilepath = f'{datepath}/{relative_to_posts}/{tofilepath}'.replace('\\', '/').replace(' ', '%20')
                print('>>>>>>>>>>>>>>>>>>>>')
                print(url, tofilepath)
                md = md.replace(url, tofilepath)
                continue
            link = url
            if link.startswith('#'): # 页内链接
                continue
            elif link.startswith('http'):
                if link.startswith(base_url):
                    topath = f'../{reurl.dirname()}/'
                else:
                    topath = '#'
            elif link.startswith('/'):
                abs_url = urljoin(base_url, link)
                topath = f'../{ResourceUrl(abs_url, src_dir, file_exts).dirname()}/'
            else:
                # 相对路径
                abs_url = urljoin(url, link)
                topath = f'../{ResourceUrl(abs_url, src_dir, file_exts).dirname()}/'
            print('url change:', url, topath)
            md = md.replace(url, topath)
        # if dir.name == 'association-between-metric-and-dichotomous-variable':
        #     stop
        md = make_tutorial(md)
        md = remove_urls(md)
        md = media_url_to_absolute(md, datepath, relative_to_posts, dir.name)
        md = make_blog(md)
        trans_count +=1
        topath = output / (mdfile.parent.name + '.md')
        topath.write_text(md, encoding='utf8')
        # copy medias
        mediasrc = mdfile.parent / 'medias'
        if mediasrc.exists():
            mediato = topath.parent / mdfile.parent.name / 'medias'
            if mediato.exists():
                shutil.rmtree(mediato)
            mediato.parent.mkdir(exist_ok=True, parents=True)
            shutil.copytree(mediasrc, mediato)

        if trans_count >= max_n:
            break
# download_whole_site(
#     'https://www.spss-tutorials.com/', 
#     'https://www.spss-tutorials.com', 
#     DOWNLOAD_DIR,
#     ignore_urls=['comment-page-'],
#     file_exts=file_exts,
# )

# translate_md(DOWNLOAD_DIR, OUTPUT_DIR, 'https://www.spss-tutorials.com', 
#              ignore_name_ptns=['-comment-page-', 'downloads-'], 
#              ignore_contents=['Error 404 - Page Not Found', 'Failed to crawl'], 
#              file_exts=file_exts, max_n=10)

# urls = extract_urls('''***Population pyramid of income_2010 by gender.** XGRAPH CHART=[HISTOBAR] BY income_2010[s] BY gender[c] /COORDINATE SPLIT=YES.

# ![SPSS Population Pyramid](https://spss-tutorials.com/img/spss-population-pyramid-unstyled.png)

# **Conclusion** : female respondents more often had incomes between $30,000 and $40,000 than males. Reversely, male respondents had incomes between $60,000 and $80,000 more often than female respondents. These are the most striking differences that account for the mean difference observed.''')
# print(urls)