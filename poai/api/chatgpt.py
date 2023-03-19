# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/8 23:39
@Description     ：
'''
import openai


def chat(api_key, prompt, model_engine="text-davinci-002", max_tokens=1024, n=1, stop=None, temperature=0.5, top_p=1,
         frequency_penalty=0.0, presence_penalty=0.6):
    # 设置 API Key
    openai.api_key = api_key  # your_api_key
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,  # 生成结果时的最大 tokens 数。平均一个汉字是 2 个 tokens，text-davinci-003 最多是 4000 个 tokens，也就是 2000 个汉字左右
        n=n,
        stop=stop,
        temperature=temperature,  # 控制结果的随机性，如果希望结果更有差异性 0.9，或者希望有固定结果可以尝试 0.0
        top_p=top_p,  # 一个可用于代替 temperature 的参数，对应机器学习中 nucleus sampling，如果设置 0.1 意味着只考虑构成前 10% 概率质量的 tokens
        frequency_penalty=frequency_penalty,  # 控制字符的重复度，取值为 -2.0 ~ 2.0 之间的数字
        presence_penalty=presence_penalty  # 控制主题的重复度，取值为 -2.0 ~ 2.0 之间的数字
    )
    # 获取 ChatGPT 的回复
    message = completions.choices[0].text
    print(message)
    return message
