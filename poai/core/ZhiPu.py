# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/3/1 23:54 
@本段代码的视频说明     ：
'''
from zhipuai import ZhipuAI


def get_response(api_key, prompt='你好，请介绍一下python-office', model="glm-4"):
    client = ZhipuAI(api_key=api_key)  # 填写您自己的APIKey
    response = client.chat.completions.create(
        model=model,  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
