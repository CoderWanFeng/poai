# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/1/18 23:27 
@本段代码的视频说明     ：
'''
from poai.core.TongYi import Tongyi


def ali(api_key: str, prompt: str):
    ty = Tongyi(api_key=api_key)
    return ty.qianwen_max(prompt)
