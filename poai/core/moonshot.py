from openai import OpenAI

from poai.lib.Const import moonshot_url


def moonshot_core(api_key, content, model,prompt):
    client = OpenAI(
        # api_key="sk-T2IKpzIxq14olNI1nJti9RZ3xcPE1G0ycumKNg7Iconda infoBreLtgDw",
        base_url=moonshot_url,
        api_key=api_key
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system","content": prompt},
            {"role": "user", "content": content}
        ]

    )
    return completion.choices[0].message.content
# TODO：
