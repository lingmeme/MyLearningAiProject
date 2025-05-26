import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), # 如果您没有配置环境变量，请在此处用您的API Key进行替换
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
)
completion = client.chat.completions.create(
    model="qwen-coder-turbo",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你好'}],
    )
# 格式化输出
print(vars(completion))
# 输出content
print(completion.choices[0].message.content)