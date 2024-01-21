# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/1/18 0:26 
@本段代码的视频说明     ：
'''

import json

import requests


class Tongyi:
    def __init__(self, api_key, model_type='qwen-max'):
        """
        初始化函数。

        参数:
            api_key (str): API密钥，开通方式：https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.72571c83RabAau
            model_type (str, 可选): 模型类型，默认为'qwen-max'。
        """

        self.api_key = api_key
        self.model_type = model_type
        self.url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'

    def qianwen_max(self, prompt: str) -> str:

        # API的URL

        # 请求头
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        # 请求体
        data = {
            "model": self.model_type,
            "input": {
                "prompt": prompt
            },
            "parameters": {}
        }

        # 将字典转换为JSON字符串
        data_json = json.dumps(data)

        # 发送POST请求
        response = requests.post(self.url, headers=headers, data=data_json)

        # 检查响应状态码
        if response.status_code == 200:
            # 解析响应内容
            response_data = response.json()
            return response_data['output']['text']
        else:
            # print(f'Error: {response.status_code}')
            return response.status_code, response.text
