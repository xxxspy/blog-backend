import subprocess
from pathlib import Path
import shutil
from aiclips.servies import askgemini
import yaml
import json

HERE = Path(__file__).parent
SRC_DIR = rootdir = HERE / 'Doing-Meta-Analysis-in-R'
TARGET_DIR = HERE / 'quarto-format'
assert rootdir.exists(), f"Root directory {rootdir} does not exist"


def clone_book():
    if SRC_DIR.exists():
        return
    cmd = ['git', 'clone', 'https://github.com/MathiasHarrer/Doing-Meta-Analysis-in-R.git']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
        raise Exception("Failed to clone book")
    else:
        print("Success:", result.stdout)


def create_project(name=TARGET_DIR.name):
    if TARGET_DIR.exists():
        TARGET_DIR.unlink()
    cmd = ['quarto', 'create-project', name, '--type', TARGET_DIR]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
        raise Exception("Failed to create project")
    else:
        print("Success:", result.stdout)

def copy_static_files():
    dirnames = ['data', 'images']
    
    for dirname in dirnames:
        src = rootdir / dirname
        dst = TARGET_DIR / dirname
        if src.exists():
            print(f"Copying {src} to {dst}")
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            raise ValueError(f"Source directory {src} does not exist")
        

def translate_llm(content: str) -> str:
    prompt = f'''
# Task
- Translate the following R Markdown content to Quarto Markdown format.
- Translate content to chinese.
-  Do not change the code chunks, only translate the text.
- Keep the original markdown structure.

# Input
<!--input begin-->
{content}
<!--input end-->

# Output
- Do not include any additional text, just the translated content.
- Use Chinese for the translation.
    '''
    response = askgemini.ask(prompt)
    return response


def translate_files():
    for srcfile in rootdir.glob('*.Rmd'):
        dstfile = TARGET_DIR / srcfile.name
        if dstfile.exists():
            print(f"Skipping {dstfile}, already exists.")
            continue
        print(f"Translating {srcfile} to {dstfile}")
        content = srcfile.read_text(encoding='utf-8')
        translated_content = translate_llm(content)
        dstfile.write_text(translated_content, encoding='utf-8')

def translate_names(files: list, title='Doing Meta Analysis in R') -> list:
    template = []
    for file in files:
        template.append({
            'href': file.name,
            'text': '<translated_title_in_chinese>',
        })
    prompt = f'''
# Task
- Translate the following names to Chinese.
- Keep the original structure.


# Output
- Output a list of translated names.
- Use json Tempalte Below, <> means the placeholder you should fill.
- Return with ```json ``` block.

# Output Template

```json
{json.dumps(template, ensure_ascii=False, indent=2)}
```
    '''
    response = askgemini.ask(prompt, True)
    return response


def make_yaml():
    srcfile = TARGET_DIR / '_quarto.yml'
    if not srcfile.exists():
        raise ValueError(f"Source file {srcfile} does not exist")
    with open(srcfile, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    mdfiles = [f for f in TARGET_DIR.glob('*.Rmd')]
    contents = translate_names(mdfiles)
    data['website']['title'] = 'R Meta 分析'
    data['website']['sidebar'] = {
        'style': 'docked',
        'search': True,
        'contents': contents
    }
    # to yaml file
    tofile = TARGET_DIR / '_quarto.yml'
    with open(tofile, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


def quarto_render():
    cmd = ['quarto', 'render']
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=TARGET_DIR)
    if result.returncode != 0:
        print("Error:", result.stderr)
        raise Exception("Failed to render quarto site")
    else:
        print("Success:", result.stdout)

def copy_to_source():
    src = TARGET_DIR / '_site'
    dst = HERE.parent.parent / 'source' / 'quarto' / 'Doing-meta-analysis-in-R'
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

if __name__ == '__main__':
    clone_book()
    create_project()
    copy_static_files()
    translate_files()
    make_yaml()
    quarto_render()
    copy_to_source()