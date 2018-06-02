from nbconvert.preprocessors.base import Preprocessor
from nbconvert import RSTExporter, MarkdownExporter
from traitlets import default
from traitlets import Unicode
import os
import re
from pathlib import Path
import nbformat as nbf
from IPython import display
import shutil

here = Path(os.path.dirname(os.path.abspath(__file__)))
source = here / 'source'
_posts = source / '_posts'



def _add_quot(cnt, indecator):
    i_len = len(indecator)
    start = 0
    in_math = False
    last_pos = -1
    insertions = []
    while True:
        i = cnt.find(indecator, start)
        if i >= 0:
            start = i + i_len
            if not in_math:
                in_math = True
                last_pos = i
            else:
                insertions.append((last_pos, i))
                in_math = False
        else:
            break
    new_content = []
    start = 0
    if insertions:
        for i, j in insertions:
            new_content.append(cnt[start:i])
            new_content.append('`'+indecator)
            new_content.append(cnt[i+i_len:j])
            new_content.append(indecator+'`')
            start = j+i_len
    else:
        new_content = [cnt]
    cnt = ''.join(new_content)
    return cnt


def mathjax(content):
    if '$$$' in content:
        raise ValueError('Not support content having more than 2 $')
    # 单行公式
    in_math = False
    last_pos = 0
    # 多行公式
    last_pos = 0
    insertions = []
    insertions2 = []
    multi_math_indecator = '____multi_math_indecator___*&^%#@___'
    mmi_len = len(multi_math_indecator)
    cnt = content.replace('$$', multi_math_indecator)
    cnt = _add_quot(cnt, '$')
    cnt = cnt.replace(multi_math_indecator, '$$')
    return _add_quot(cnt, '$$')


def extract_images(content):
    if not content:
        return
    html_ptn = re.compile('src="(?P<s>.+?)"')
    md_ptn = re.compile('\!\[.+?\]\((.+?)\)')
    assets = []
    assets.extend(html_ptn.findall(content))
    assets.extend(md_ptn.findall(content))
    return [a.strip() for a in assets if 'http://' not in a and 'https://' not in a]


class HexoExporter(MarkdownExporter):
    template_file = './markdown.tpl'

    def default_filters(self):
        filters = list(super().default_filters())
        filters.append(('mathjax', mathjax))
        return filters

    def _template_file_default(self):
        return 'markdown'

    @property
    def template_path(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path + [str(here)]


def _add_infos(body, notebook_link, qq='675495787'):
    info = (f'\n\n> **注意**\n'
            f'> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook]({notebook_link})\n'
            f'> 有问题可以直接在下方留言\n'
            f'> 或者给我发邮件{qq}[at]qq.com\n'
            f'> 请记住我的网址: mlln.cn 或者 jupyter.cn\n')
    body += info
    return body

def to_hexo(notebook_file, with_images=True, with_assets=False):
    nb_path = Path(notebook_file)
    nb = nbf.read(notebook_file, nbf.NO_CONVERT)
    mde = HexoExporter()
    body, resources = mde.from_notebook_node(nb)
    name = nb_path.name
    if name.endswith('.ipynb'):
        name = name[:-6]
    asset_dir = _posts / name
    # 复制所有文件
    nb_dir = Path(notebook_file).parent
    asset_dir.mkdir(exist_ok=True)
    for out in resources.get('outputs', []):
        des = asset_dir / out
        des.write_bytes(resources['outputs'][out])
        print(f'copy filt to {des}')

    # 把notebook复制到hexo
    des = asset_dir / (name + '.ipynb')
    print(nb_path, des)
    shutil.copy(nb_path, des)
    print(f'copy file to {des}')
    # 复制其他
    if with_assets:
        # 把notebook所在文件夹下的所有文件都复制到hexo asset文件夹下
        f: Path
        for f in nb_dir.iterdir():
            des = asset_dir / f.name
            if f.is_file():
                shutil.copy(f, des)
            else:
                shutil.copytree(f, des)
    elif with_images:
        for img in extract_images(body):
            src = nb_dir / img
            des = asset_dir / img
            des.parent.mkdir(exist_ok=True, parents=True)
            if src.exists():
                print(f'copy file to {des}')
                shutil.copy(src, des)
    
    # 生成markdown
    body = _add_infos(body, nb_path.name)
    fpath = _posts / (name + '.md')
    fpath.write_text(body, encoding='utf8')


if __name__ == '__main__':
    notebook_file = r'D:\mysites\notebooks\[转]吊炸天的中文自然语言处理工具和语料库介绍.ipynb'
    to_hexo(notebook_file)
