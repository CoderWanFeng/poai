# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/8 23:39
@Description     ：
'''
import unittest

from poai.api.chatgpt import *


class TestTools(unittest.TestCase):
    def test_chat(self):
        chat(api_key='', prompt='')
