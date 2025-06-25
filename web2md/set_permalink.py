from pathlib import Path
import re
import yaml


def set_permalink(md_path):
    text = Path(md_path).read_text(encoding='utf-8')
    # 匹配 YAML front matter
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        print("No YAML front matter found.")
        return
    yaml_str = m.group(1)
    body = text[m.end():]
    data = yaml.safe_load(yaml_str)
    date = data.get('date', None)
    if not date:
        return
    # date 2016-04-05 18:17:17 to path 2016/04/05
    if isinstance(date, str):
        return
    date_path = date.strftime('/%Y/%m/%d')
    data['permalink'] = f"{date_path}/{md_path.stem}/"
    new_yaml = yaml.dump(data, allow_unicode=True, sort_keys=False).strip()
    new_text = f"---\n{new_yaml}\n---\n{body}"
    Path(md_path).write_text(new_text, encoding='utf-8')


def set_all_links():
    source_dir = Path(__file__).parent.parent / 'source/_posts'
    for md_file in source_dir.rglob('*.md'):
        if 'permalink' not in md_file.read_text(encoding='utf-8'):
            print(f"Setting permalink for {md_file}")
            set_permalink(md_file)

if __name__ == '__main__':
    set_all_links()