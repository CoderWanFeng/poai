# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/12/5 21:35 
@本段代码的视频说明     ：
'''
from poai.core.AIArt import get_text2image_result


def text2image(id, key, prompt: str, output: str = r'./text2image.jpg'):
    """
    1行代码，生成AI绘画
    :param id: 腾讯云的id，开通方式：https://curl.qcloud.com/gyWD7glH
    :param key: 腾讯云的key，开通方式：https://curl.qcloud.com/gyWD7glH
    :param prompt: 关于图片的描述文本，将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。
                    不能为空，推荐使用中文。最多可传256个 utf-8 字符。
    :param output: 输出图片的位置和名称。
    :return:
    """
    get_text2image_result(id, key, prompt, output)
