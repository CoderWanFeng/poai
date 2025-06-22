# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@代码日期    ：2024/1/18 23:27 
@本段代码的视频说明     ：
'''

from poai.core.DeepSeek import get_response_from_deepseek_in_tx
from poai.core.TongYi import Tongyi
from poai.core.ZhiPu import get_response


def ali(api_key: str, prompt: str):
    """
    调用大模型
    :param api_key:
    :param prompt:
    :return:
    """
    ty = Tongyi(api_key=api_key)
    return ty.qianwen_max(prompt)


def zhipu(api_key, prompt='你好，请介绍一下python-office', model="glm-4"):
    # https://open.bigmodel.cn/dev/api#overview
    return get_response(api_key, prompt, model)


def deepseek(api_key, content, origin=False, tx=True):
    if tx:
        return get_response_from_deepseek_in_tx(api_key, content)

