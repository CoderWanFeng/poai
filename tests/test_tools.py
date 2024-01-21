# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/8 23:39
@Description     ：
'''
import os
import unittest

from poai.api.aiart import text2image
from poai.api.chatgpt import *


class TestTools(unittest.TestCase):
    def test_chat(self):
        chat(api_key='', prompt='')
    def test_text2img(self):
        # 说明文档：https://mp.weixin.qq.com/s/-rx03ewvRieaFTDwbAmzOw
        text2image(id=os.getenv("SecretId"), key=os.getenv("SecretKey"), prompt="女朋友", output= r'./output/text2image.jpg')
