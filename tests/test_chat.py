# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@代码日期    ：2024/1/20 0:17 
@本段代码的视频说明     ：
'''
import os
import unittest

from poai.api.chat import *


class TestTools(unittest.TestCase):
    def test_ali(self):
        # 替换为你的API密钥
        api_key = os.getenv("TY_KEY")  # 此处填入你的api-key
        print(ali(api_key, prompt='你好'))

    def test_zhipu(self):
        # 替换为你的API密钥
        api_key = ''  # 此处填入你的api-key
        print(zhipu(api_key))

    def test_deepseek(self):
        print(deepseek(api_key='sk-pRdhASKn0wm5i7DjkdDfj5ENbRcpsqGrtV7hdFZZ6laV5aMk', content='你好'))

    def test_moonshot(self):
        api_key="sk-T2IKpzIxq14olNI1nJti9RZ3xcPE1G0ycumKNg7IBreLtgDw"
        comtent="夏天推荐吃什么水果？"
        for chunk in moonshot(api_key,comtent):
            print(chunk,end="")
