from openai import OpenAI


def moonshot(api_key, content):
    client = OpenAI(
        # api_key="sk-T2IKpzIxq14olNI1nJti9RZ3xcPE1G0ycumKNg7IBreLtgDw",
        base_url="https://api.moonshot.cn/v1",
        api_key=api_key,

    )

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": "你的名字是：小A。你的回答总是极为简洁，如果用户向你提问，你只需要回答答案即可"},
            # {"role": "user", "content": "为什么夏天的西瓜会便宜？"}
            {"role": "user", "content": content}
        ],
        stream=True #流式调用
    )
    for chunk in completion:
        yield chunk.choices[0].delta.content # 流式输出
    # print(completion.choices[0].message.content)
