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

@memory.cache
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
    if not output_dir.exists(): output_dir.mkdir()
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url, screenshot=True)
        if result.screenshot:
            ssfpath = output_dir / 'screenshot.png'
            ssfpath.write_bytes(base64.b64decode(result.screenshot))
        outfpath = output_dir / outfname
        markdown = result.markdown
        resdata = {
            'images': result.media['images'],
            'videos': result.media['videos'],
        }
        resultpath = output_dir / CrawResultFileName
        resultpath.write_text(json.dumps(resdata, ensure_ascii=False), encoding='utf8')
        medias = []
        mediadir = output_dir / 'medias'
        mediadir.mkdir(exist_ok=True)
        for img in result.media['images'] + result.media['videos']:
            src = img['src']
            # download image from url
            # turn relative url to absolute url
            if src.startswith('http'):
                absurl = src
            else:
                absurl = url.strip('/') + '/' + src.strip('/')
            suffix = src.split('.')[-1]
            shortname = str_compress(src)
            imgpath = mediadir / f'{shortname}.{suffix}'
            medias.append(imgpath)
            if imgpath.exists() and not redownload: continue
            data = requests.get(absurl).content
            imgpath.parent.mkdir(parents=True, exist_ok=True)
            imgpath.write_bytes(data)
            markdown = markdown.replace(src, f'medias/{shortname}.{suffix}')
    outfpath.write_text(markdown, encoding='utf-8')
    return [outfpath,medias,]
            
@memory.cache
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


def remove_urls(content: str):
    prompt = f'''# 任务
- 我不希望文章中包含其他网站的链接
- 请删除网页链接/并修改内容为合理的格式
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
    
@memory.cache
def download_replace_imgs(content: str, mediadir: Path):
    # 使用正则表达式提取所有图片链接（支持 Markdown 格式 ![alt](url)）
    pattern = r'!\[.*?\]\((.*?)\)'
    imgs = re.findall(pattern, content)
    for img in imgs:
        if img.startswith('http'):
            filepath = _download_img(img, mediadir)
            relative_path = filepath.relative_to(mediadir.parent)
            content = content.replace(img, relative_path.as_posix())
    print(content)
    # 迭代mediadir下的图片文件, 为图片添水印
    for imgfile in mediadir.glob('*'):
        if imgfile.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
            continue
        with Image.open(imgfile).convert("RGBA") as im:
            if im.size[0]<200:continue
            txt_layer = Image.new("RGBA", im.size, (255,255,255,0))
            draw = ImageDraw.Draw(txt_layer)
            font_size = max(16, im.size[0] // 40)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            text = "mlln.cn"
            bbox = draw.textbbox((0, 0), text, font=font)
            textwidth = bbox[2] - bbox[0]
            textheight = bbox[3] - bbox[1]
            x = im.size[0] - textwidth - 10
            y = im.size[1] - textheight - 10
            draw.text((x, y), text, font=font, fill=(255,255,255,128))
            watermarked = Image.alpha_composite(im, txt_layer)
            if imgfile.suffix.lower() in ['.jpg', '.jpeg']:
                watermarked = watermarked.convert("RGB")
            watermarked.save(imgfile)
    return content

@memory.cache
def make_tutorial(mdcontent: str):
    prompt = f'''# 任务
- 根据原文章翻译或者撰写为一篇中文文章
- 生成符合中文阅读习惯的教程
- 如果是专业术语/软件界面文字或其他关键词, 你需要保留中文和英文, 方便读者理解

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
def get_category(content: str)->str:
    cats = json.loads((HERE/'stats-cats.json').read_text('utf8'))
    str_cats = []
    for c1 in cats:
        for c2 in c1['subcategories']:
            str_cats.append(f'{c1["category"]}/{c2["name"]}')
    str_cats = '\n'.join(str_cats)
    prompt = f'''# 任务
- 从以下类别中选择一个最适合文章内容的类别
- 如果文章内容涉及多个类别, 请优先选择最相关的类别
- 如果找不到合适的类别, 请返回"其他"

# 类别列表
{str_cats}

# 原文

<!-- 原文开始 -->
{content}
<!-- 原文结束 -->

# 输出

仅输出分类列表中的类名, 不要返回其他内容
'''
    response = completion(
        model="gemini/gemini-2.0-flash", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

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

def get_summary(content):
    '''总结文章, 生成一段简短的引言性总结, 适合用于文章预览, 字数少于100字'''
    prompt = f'''# 任务
- 请根据下文内容，生成一段简短的中文引言性总结，适合用于文章预览
- 字数不超过100字

# 原文

<!-- 原文开始 -->
{content}
<!-- 原文结束 -->

# 输出

仅输出总结内容，不要输出其他内容
'''
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()


def remake(url: str):
    dirname = str_compress(str(url))
    output_dir = HERE / '.outputs' / dirname
    output_dir.mkdir(exist_ok=True, parents=True)
    mediadir = output_dir / 'medias'
    mdfile, medias = sync_web2markdown(url, output_dir)
    print(mdfile)
    content = make_tutorial(mdfile.read_text('utf8'))
    content = remove_urls(content)
    print(content)
    download_replace_imgs(content, mediadir)
    cat = get_category(content).strip().split('\n')[0]
    title = get_title(content).strip()
    post_fpath = SOURCE_DIR / cat / f'{title}.md'
    if post_fpath.exists() and post_fpath.is_dir():
        post_fpath.rmdir()
    post_fpath.parent.mkdir(parents=True, exist_ok=True)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    tags = cat.replace('/', ',')
    mdcontent = f'''---
title: {title}
date: {date}
tags: [{tags}]
author: mlln.cn
---

{get_summary(content)}

<!-- more -->

{content}
'''
    post_fpath.write_text(mdcontent, encoding='utf8')
    target_mediadir = post_fpath.parent / title / 'medias'
    # copy mediadir to target_mediadir
    if mediadir.exists():
        shutil.copytree(mediadir, target_mediadir, dirs_exist_ok=True)





if __name__ == '__main__':
    remake('https://www.spss-tutorials.com/spss-data-editor-window/')