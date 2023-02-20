# -*- coding: UTF-8 -*-
'''
@Author  ：devinglaw
@Up  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/20 20:47 
@Description     ：
'''

import poai


def chatgpt(question):
    poai.chatgpt.chat(api_key='你的API_KEY', prompt=question)


if __name__ == '__main__':
    while True:
        print("聊天机器人的交流群是：https://mp.weixin.qq.com/s/6cR5fMSCtdI5sJdWiDwhOA")
        print("我是机器人ChatGPT，请输入您要咨询的问题:")
        print()
        chatgpt(question=input())
        print("我是机器人ChatGPT，请输入您要咨询的问题:")
        q = input("聊天请继续，退出请输入：q")
        print()
        if "q" == q:
            break
