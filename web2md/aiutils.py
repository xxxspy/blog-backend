from litellm import completion as _completion
from joblib import Memory
import time, json, re
from dotenv import load_dotenv
from pathlib import Path

HERE = Path(__file__).parent

load_dotenv(HERE/'.envs')

memory = Memory('.cache')
def rest_and_retry(func, *args, **kwargs):
    while True:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            time.sleep(60)


def parse_json(text: str):
    text = text.split('```')[1][4:].strip()
    if text.startswith('json'):
        text = text[4:].strip()
    try: 
        data =json.loads(text)
    except json.decoder.JSONDecodeError:
        text = re.sub(r',\s*([\]}])', r'\1', text)
        data = json.loads(text)
    return data

@memory.cache
def ask(prompt: str, response_json=False, model='gemini/gemini-2.0-flash'):
    resp = rest_and_retry(
        _completion,
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    resp = resp.choices[0].message.content
    if response_json:
        resp = parse_json(resp)
    return resp