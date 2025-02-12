# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/1/17 22:40 
@本段代码的视频说明     ：
'''
import json
import os

import requests


def tongyi_api(text: str, api_key: str, model_type='qwen-max') -> str:
    """
    调用同义词API对给定的文本进行处理。

    参数:
        text (str): 需要处理的文本。
        api_key (str): API密钥。
        model_type (str, optional): 模型类型，默认为我们使用通义千问限时免费的qwen-max模型

    返回:
        str: 处理后的文本。
    """

    # API的URL
    url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'

    # 请求头
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # 请求体
    data = {
        "model": model_type,
        "input": {
            "prompt": text
        },
        "parameters": {}
    }

    # 将字典转换为JSON字符串
    data_json = json.dumps(data)

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data_json)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析响应内容
        response_data = response.json()
        print(response_data['output']['text'])
    else:
        print(f'Error: {response.status_code}')
        print(response.text)


if __name__ == '__main__':
    while True:
        text = input('请输入要处理的文本：')
        if text == 'q':
            break

        # 替换为你的API密钥
        api_key = os.getenv("TY_KEY")  # 此处填入你的api-key

        tongyi_api(api_key=api_key, text=text)
