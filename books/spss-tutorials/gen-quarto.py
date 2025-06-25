import sys
from pathlib import Path
import shutil
sys.path.insert(0, r'./web2md')
from site2quarto import main, move_static

BLOG_ROOT = Path(r'D:\dev\blog-backend')
toroot = BLOG_ROOT / r'web2md\.outputs\spss-quarto'
fromroot = BLOG_ROOT / r'web2md\.outputs\spss-tutorials-html\spss-tutorials.com'

navbar_links = [
    {
        'text': '网站首页',
        'href': 'https://mlln.cn',
    },
    {
        'text': 'SPSS终极教程',
        'href': 'index.md',
    },
    {
        'text': '数据文件下载',
        'href': 'download.md',
    },
    {
        'text': '关于我们',
        'href': 'about.md',
    },
    {
        'text': '统计咨询',
        'href': 'zixun.md',
    }
]
main(toroot, fromroot, 'spss-tutorials.com', content_selector='#the-content', title_selector='#main-title', 
        rootpath='',
        file_share_link='https://pan.quark.cn/s/a68aec661fff',
        navbar_links=navbar_links
    )

# move files
HERE = Path(__file__).parent
for nl in navbar_links:
    fname = nl['href']
    if fname.endswith('.md'):
        shutil.copy(HERE / fname, toroot / fname)

index = HERE / 'index.qmd'
if index.exists():
    index.unlink()