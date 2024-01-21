# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/1/20 0:17 
@本段代码的视频说明     ：
'''
import os
import unittest

from poai.api.chat import ali


class TestTools(unittest.TestCase):
    def test_chat(self):
        # 替换为你的API密钥
        api_key = os.getenv("TY_KEY")  # 此处填入你的api-key
        print(ali(api_key, prompt='你好'))
