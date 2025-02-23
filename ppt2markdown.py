from pptx2md import convert, ConversionConfig

from pathlib import Path
from aiclips.servies import askgemini

# Basic usage

def pdf2tutorial(
        pptx_path,
        output='ppt-convert/ppt-convert.md', 
        image_dir='ppt-convert/img',
        tutorial_path='ppt-convert/tutorial.md'
):
    pptx_path=Path(pptx_path)
    output=Path(output)
    image_dir=Path(image_dir)
    convert(ConversionConfig(pptx_path=pptx_path, output_path=output, image_dir=image_dir, disable_notes=True))
    md = output.read_text(encoding='utf8')
    prompt = f'''
<!-- PPT内容 -->
{md}
<!-- PPT内容结束 -->

# 任务
- 根据PPT内容写一篇中文教程
- 补充细节: 如果PPT内容过于简短请补充细节, 使之更像一篇教程
- 输出格式: markdown
- 尽量保留图片内容
- 返回教程内容, 不要返回其他内容
'''
    tutorial = askgemini.ask(prompt)
    Path(tutorial_path).write_text(tutorial, encoding='utf8')

pdf2tutorial(Path('d:/download/Two-level multilevel model (illustration from chapter 3 Heck et al., 2014)-3a (1).pptx'))