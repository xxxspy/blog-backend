from pathlib import Path
from pyquery import PyQuery as pq
from aiutils import ask
import yaml, json
from crawl4ai.html2text import HTML2Text
from joblib import Memory
import subprocess
import shutil
import re
from urllib.parse import urlparse
import hashlib


memory = Memory('.cache')


def format_mathjax(html: str) -> str:
    '''删除 span.MathJax 标签及其内容'''
    doc = pq(html)
    doc('span.MathJax').remove()
    # 替换 <script type="math/tex; mode=display" 或者 <script type="math/tex" jiang script 替换为<div>标签
    for script in doc('script[type^="math/tex"]'):
        s = pq(script)
        math_content = s.text()
        mode = s.attr('type')
        if mode and 'mode=display' in mode:
            span = f'<span class="math display">$$ {math_content} $$</span>'
        else:
            span = f'<span class="math inline">${math_content}$</span>'
        s.replace_with(span)
    return str(doc)


def to_markdown(html:str, content_selector: str, format_mathjax_func=None):
    content = pq(html).find(content_selector)
    if format_mathjax_func is not None:
        content = format_mathjax_func(content)
    content = str(content)
    converter = HTML2Text()
    return converter.handle(content)


@memory.cache
def make_tutorial(mdcontent: str):
    prompt = f'''# 任务
- 根据原文章翻译或者撰写为一篇中文文章
- 生成符合中文阅读习惯的教程
- 如果是专业术语/软件界面文字或其他关键词, 你需要保留中文和英文, 方便读者理解
- 不要更改链接
- 生成的内容符合 quarto 文章的markdown格式

# 原文
<!-- 原文开始 -->
{mdcontent}
<!-- 原文结束 -->

# 输出
仅输出中文文章教程, 不要输出其他任何内容, 不要输出客套语
'''
    response = ask(prompt)
    return response


def htmldir_to_md(htmldir: Path, content_selector, title_selector='title', suffix='.html', 
             format_mathjax_func=None, 
             translate_func=None)->list[tuple]:
    filetitles = []
    for fp in htmldir.rglob('*'+suffix):
        html = fp.read_text('utf8')
        html = pq(html)
        content = html.find(content_selector)
        if not content:
            content = html.find('body')
        if format_mathjax_func is not None:
            content = format_mathjax_func(content)
        content = str(content)
        md_content = HTML2Text().handle(content)
        title = html.find(title_selector)
        if not title:
            title = html.find('title')
        title = title.text()
        if translate_func is not None:
            md_content = translate_func(f'# {title}\n\n'+md_content)
        mdfile = fp.with_suffix('.md')
        mdfile.write_text(md_content, encoding='utf8')
        filetitles.append({'title': title, 'path': mdfile.relative_to(htmldir).as_posix()})
    return filetitles
        
@memory.cache
def tree_translate(tree: list[dict]):
    prompt = f'''# 任务
- 以下是网站目录的一个树形结构
- 翻译标题"title"部分, 但是不要翻译文件路径

# 目录
```json
{json.dumps(tree, ensure_ascii=False)}
```

# 返回
返回翻译后的目录树, 保持结构不变, 返回json, 不要返回其他任何内容
'''
    res = ask(prompt, response_json=True)
    return res

def str_compress(long_string : str, length=30)->str:
    """压缩字符串"""
    # 使用 MD5 哈希函数
    hash_object = hashlib.md5(long_string.encode('utf8'))
    # 获取哈希值的十六进制表示
    hex_dig = hash_object.hexdigest()
    # 截取前20个字符
    compressed_string = hex_dig[:length]
    return compressed_string


def move_static(mdcontent: str, fromroot: Path, relative: Path, toroot: Path, hostname: str, rootpath: str='', file_share_link=''):
    '''将 mdcontent (markdown) 中的静态文件从fromdir移动到mddir, 替换mdcontent中的链接路径
    fromroot: 来源根目录
    relative: 来源md文件相对于fromroot的路径
    toroot: 目的地md文件的路径根目录
    hostname: 要处理的链接的主机域名
    rootpath: 新服务器中, 页面文件存放的跟路径, 比如 /book
    file_share_link: 网盘分享链接, 用于存放数据文件等非图片文件
    '''
    # 匹配 Markdown 链接: [text](url)
    pattern = re.compile(r'!\[.*?\]\((.*?)\)|\[[^\]]*\]\((.*?)\)', re.DOTALL)
    # 提取所有链接（图片和普通链接），合并分组结果
    links = []
    # mdcontent = Path(r'D:\dev\blog-backend\web2md\.outputs\spss-quarto\cohens-d\index.md').read_text('utf8')
    for m in pattern.findall(mdcontent):
        link = m[0] or m[1]
        if link:
            links.append(link)
    frompath = fromroot / relative
    fromdir = frompath.parent
    topath = toroot / frompath.relative_to(fromroot)

    for link in links:
        parsed = urlparse(link)
        link_host = parsed.hostname
        if link_host and hostname not in link_host:
            continue
        
        if parsed.path.startswith('/'):
            link_path = (fromroot / parsed.path.lstrip('/')).resolve()
        else:
            link_path = (fromdir / parsed.path).resolve()
        def is_img(link_path: Path)->bool:
            """判断链接是否指向图片文件"""
            return link_path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'}
        if link_path.exists(): 
            if link_path.is_file():
                if file_share_link and not is_img(link_path):
                    to_path = toroot / '_shared_files'/ Path(relative).parent.as_posix() / Path(parsed.path).name
                    to_path.parent.mkdir(parents=True, exist_ok=True)
                    replace_link = file_share_link
                else:
                    newname = f'{str_compress(parsed.path)}{Path(parsed.path).suffix}'
                    to_path = topath.parent / newname
                    to_path.parent.mkdir(parents=True, exist_ok=True)
                    replace_link = f'./{newname}'
                shutil.copy2(link_path, to_path)
                mdcontent = mdcontent.replace(link, replace_link)
            else:
                abslink = f'{rootpath.rstrip("/")}/{link_path.relative_to(fromroot).as_posix()}'
                mdcontent = mdcontent.replace(link, abslink)
    return mdcontent


@memory.cache
def gen_tree(filetitles: list[tuple])->list[dict]:
    yaml_titles = yaml.dump(filetitles)
    prompt = f'''# 标题和文件路径
```yaml
{yaml_titles}
```

# 任务
- 使用前面的标题和文件路径组织网站目录
- 目录和文章的顺序遵循先易后难/从简单到复杂/从入门到精通/从正文到附录的原则
- 使用三级标题
- 使用yaml格式输出, 遵循quarto的配置文件格式
- 模仿下面的输出模板, <> 代表占位符, 不可更改关键词

# 输出模板
```yaml
- section: <name of this section>
  contents:
  - section: <name of this subsection>
    contents:
    - href: <path to the md file>
      text: <title of the md file>
    - href: <path to the md file2>
      text: <title of the md file2>
  - section: <name of this subsection2>
    contents:
    - href: <path to the md file3>
      text: <title of the md file3>
- section: <name of this section2>
  contents:
  - section: <name of this subsection3>
    contents:
    - href: <path to the md file4>
      text: <title of the md file4>
```
'''
    tree = ask(prompt)
    tree = tree.split('```yaml')[-1]
    tree = tree.split('```')[0]
    # 使用 yaml 库加载
    return yaml.safe_load(tree)

def main(
        toroot: Path, 
        fromroot: Path, 
        hostname: str, 
        rootpath='/', 
        content_selector='body', 
        title_selector='title', 
        suffix='.html', 
        format_mathjax_func=format_mathjax, 
        translate_func=make_tutorial,
        quarto_title='SPSS 终极教程',
        file_share_link='', #网盘分享链接, 用于存放数据文件等非图片文件
        navbar_links = [], # list of dict, {'text': 'link text', 'href': 'link url'}, 生成的quarto网站的header链接, 默认是空列表
        ):
    # 创建 quarto site
    if toroot.exists():
        shutil.rmtree(toroot)
    toroot.mkdir(parents=True, exist_ok=True)
    subprocess.run(['quarto', 'create-project', '--type', 'website', str(toroot)], check=True)
    # html 转 md
    filetitles = htmldir_to_md(fromroot, content_selector, title_selector, suffix=suffix, format_mathjax_func=format_mathjax_func, translate_func=translate_func)
    tree = gen_tree(filetitles)
    tree = tree_translate(tree)

    # 生成 _quarto.yaml
    with open(toroot / '_quarto.yml', 'r', encoding='utf8') as f:
        config = yaml.safe_load(f)
    config['website']['sidebar'] = {
        'style': 'docked',
        'search': True,
        'contents': tree,
    }
    config['website']['title'] = quarto_title
    config['project']['render'] = ["*.md", ]
    config['website']['navbar'] = {'left': navbar_links}
    with open(toroot / '_quarto.yml', 'w', encoding='utf8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)
    # 复制所有 md 文件
    for fp in fromroot.rglob('*.md'):
        topath = toroot / fp.relative_to(fromroot)
        topath.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy(fp, topath)
    # 移动静态文件, 更改md文件中的链接
    for fp in toroot.rglob('*.md'):
        relative = fp.relative_to(toroot)
        mdcontent = move_static(fp.read_text('utf8'), fromroot, relative, toroot, hostname, rootpath, file_share_link)
        fp.write_text(mdcontent, encoding='utf8')
    







if __name__ == '__main__':
    toroot = Path(r'D:\dev\blog-backend\web2md\.outputs\spss-quarto')
    fromroot = Path(r'D:\dev\blog-backend\web2md\.outputs\spss-tutorials-html\spss-tutorials.com')
    main(toroot, fromroot, 'spss-tutorials.com', content_selector='#the-content', title_selector='#main-title', 
         rootpath='',
         file_share_link='https://pan.quark.cn/s/a68aec661fff')