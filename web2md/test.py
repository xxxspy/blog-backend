from litellm import completion
from pathlib import Path
from dotenv import load_dotenv

HERE = Path(__file__).parent

load_dotenv(HERE/'.envs')

system = '你是一个犀利的视频评论员, 人狠话不多, 语言具有吸引力和煽动性'
# system = '你是一个犀利的视频评论员, 你是诺贝尔文学奖获得者莫言, 语言具有吸引力和煽动性'
message = '我一生善良, 没有做过什么坏事, 怎么人生的苦难我一件也没有错过'

response = completion(
    model="gemini/gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": message}
    ]
)
print(response['choices'][0]['message']['content'])