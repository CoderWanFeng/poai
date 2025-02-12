# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2025/2/11 20:39 
@本段代码的视频说明     ：
'''

from openai import OpenAI


def get_response_from_deepseek_in_tx(api_key, content):
    # 构造 client
    client = OpenAI(
        api_key=api_key,  # 知识引擎原子能力 APIKey
        base_url="https://api.lkeap.cloud.tencent.com/v1",
    )
    # 流式
    s_value = False
    # 请求
    chat_completion = client.chat.completions.create(
        model="deepseek-r1",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        stream=s_value,
    )
    if s_value:
        for chunk in chat_completion:
            # 打印思维链内容
            if hasattr(chunk.choices[0].delta, 'reasoning_content'):
                pass
                # print(f"{chunk.choices[0].delta.reasoning_content}", end="")
            # 打印模型最终返回的content
            if hasattr(chunk.choices[0].delta, 'content'):
                if chunk.choices[0].delta.content != None and len(chunk.choices[0].delta.content) != 0:
                    print(chunk.choices[0].delta.content, end="")
    else:
        result = chat_completion.choices[0].message.content
    return result


if __name__ == '__main__':
    get_response_from_deepseek_in_tx("sk-pRdhASKn0wm5i7DjkdDfj5ENbRcpsqGrtV7hdFZZ6laV5aMk", "你好")
