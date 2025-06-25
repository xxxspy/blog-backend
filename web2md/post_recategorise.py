'''将文章分类'''
from pathlib import Path
import json
from litellm import completion
import dotenv
from math import ceil
import time
from functools import wraps
from joblib import Memory
memory = Memory('.cache')

HERE = Path(__file__).parent
POST_DIR = HERE.parent / 'source/_posts'
dotenv.load_dotenv(HERE.parent/'.envs')
stop
categories = json.loads((HERE / 'stats-cats.json').read_text('utf8'))

def sleep_retry(func):
    max_retries=10
    sleep_seconds=10
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(sleep_seconds)
    return wrapper
completion = sleep_retry(completion)

names = []
for post in POST_DIR.glob('*.md'):
    names.append(post.stem)
names = '\n'.join(names)

def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

all_names = names.split('\n')

all_cats = {}

@memory.cache
def get_cat(chunk: list):
    prompt = f'''# 任务
- 提取文章类别
- 能看出软件名称, 提取软件的名称作为分类名
- 不能看出软件名称的以算法分类,需要识别出具体算法名称
- 其他文章按照你认为合理的方式分类

# 题目
{chr(10).join(chunk)}

# 输出
- 文章名和类别名的对应关系
- 使用json格式
- 按照json模板的格式输出

<!-- json模板 -->
```json
{{
    "文章名1": "类别名1",
    "文章名2": "类别名2"
}}
```
<!-- json模板结束 -->
'''
    response = completion(
        model="gemini/gemini-2.0-flash", 
        messages=[{"role": "user", "content": prompt}]
    )
    cats = response['choices'][0]['message']['content'].strip().strip('`').strip('json').strip()
    cats = json.loads(cats)
    print(cats)
    return cats

for chunk in chunk_list(all_names, 50):
    all_cats.update(get_cat(chunk))
    print('============')

postcats = HERE / 'posts.json'
postcats.write_text(json.dumps(all_cats, ensure_ascii=False, indent=2), encoding='utf8')