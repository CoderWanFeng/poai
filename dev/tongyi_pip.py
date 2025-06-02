# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@代码日期    ：2024/1/20 0:14 
@本段代码的视频说明     ：
'''
import os

import poai

#
# ty = Tongyi(api_key=api_key)
#
# reply = ty.qianwen_max("你好啊")
# print(reply)
# tongyi_api(api_key=api_key, text=text)


api_key = os.getenv("TY_KEY")  # # 替换为你的API密钥
api_key = 'dfjasjdlfJJ98jjaaa'  # 替换为你的API密钥
res = poai.chat.ali(api_key, prompt='请写一段python代码，输出九九乘法表')  # 调用ali函数，传入api_key和prompt参数，获取返回结果
print(res)  # 打印返回结果
