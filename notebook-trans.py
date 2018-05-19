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


# class HexoProcessor(Preprocessor):

#     def __remove_requirejs(self, html):
#         ptn = re.compile(
#             '<script>\n    require.config\(([\s\S]+?)\);\n\</script\>\n', re.M)
#         m = ptn.search(html).group(0)
#         lines = m.split('\n')[3:-4]
#         scripts = [l.strip().replace("'", "") for l in lines]
#         scripts = [l.split(':')[-1].strip() for l in scripts]
#         rtn = []
#         echart_common = '<script src="https://cdn.bootcss.com/echarts/4.0.4/echarts-en.common.js"></script> '
#         for s in scripts:
#             if s.endswith('echarts.min'):
#                 rtn.append(echart_common)
#             else:
#                 raise NotImplementedError(
#                     'This JS not processed: {}'.format(s))

#         require_ptn = re.compile("  require\(.*, function\(.*\) {")
#         require_ender = re.compile('\}\);\n\</script\>\n$', re.M)
#         html = ptn.sub('', html)
#         html = require_ptn.sub('', html)
#         html = require_ender.sub('</script>', html)
#         html = '\n'.join(rtn) + html
#         return html

#     def _rm_requirejs(self, chartscript):
#         '''remove thre requireJS.
#         This hard coding strings came from
#         (pyecharts:v1.33)[https://github.com/pyecharts/pyecharts/blob/master/pyecharts/templates/notebook.html],
#         If the `pyecharts/templates/notebook.html` changed, this method would fail.
#         '''
#         starter = '<script>\n    require.config({\n        paths: {\n'
#         ender = '});\n</script>\n'
#         ptn = re.compile('require.config\([\s\S]+?\);\n\</script\>\n', re.M)
#         if chartscript.startswith(starter) \
#                 and chartscript.endswith(ender) \
#                 and ptn.search(chartscript):
#             return self.__remove_requirejs(chartscript)

#     def preprocess_cell(self, cell, resources, cell_index):
#         '''处理总流程'''
#         assets = self._extract_assets_from_markdown(cell)
#         if assets:
#             if 'assets' in resources:
#                 resources['assets'].extend(assets)
#             else:
#                 resources['assets'] = assets
#         print('resources:', resources)

#         return cell, resources

#     def _extract_assets_from_markdown(self, cell):
#         '''因为有些静态文件并不会被处理, 所以我们需要复制这些文件到hexo assets文件夹
#         , 但是该方法只是提取文件名, 复制文件需要在导出(export)以后再处理'''
#         if cell.cell_type != 'markdown':
#             return
#         source = cell.get('source', '')
#         if not source:
#             return
#         html_ptn = re.compile('\<img.+src="(.+?)".+/\>')
#         md_ptn = re.compile('\!\[.+?\]\((.+?)\)')

#         assets = []
#         assets.extend(html_ptn.findall(source))
#         assets.extend(md_ptn.findall(source))
#         return [a.strip() for a in assets if 'http://' not in a and 'https://' not in a]


# # mde.preprocessors.append(HexoOutputProcessor)
# notebook_file = r'D:\mysites\deeplearning.ai-master\Convolutional Neural Networks\week1\卷积神经网络逐步实现.ipynb'
# nb = nbf.read(notebook_file, nbf.NO_CONVERT)
# mde = MarkdownExporter()
# mde.register_preprocessor(HexoProcessor, enabled=True)
# print(mde.preprocessors)
# stop
# body, resources = mde.from_notebook_node(nb)
# print(resources.keys())
# print(resources['outputs'].keys())
# print('finall assets:', resources['assets'])


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
            if src.exists():
                print(f'copy file to {des}')
                shutil.copy(src, des)
    
    # 生成markdown
    body = _add_infos(body, nb_path.name)
    fpath = _posts / (name + '.md')
    fpath.write_text(body, encoding='utf8')


if __name__ == '__main__':
    notebook_file = r'D:/mysites/notebooks/python3 f-string格式化字符串的高级用法.ipynb'
    to_hexo(notebook_file)
