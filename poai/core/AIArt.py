# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/12/5 21:35 
@本段代码的视频说明     ：
'''

import base64
import json
from io import BytesIO
from pathlib import Path
import os
from PIL import Image
from tencentcloud.aiart.v20221229 import aiart_client, models
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def get_text2image_result(id, key, prompt, output):
    # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
    # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/127
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取

        cred = credential.Credential(id, key)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "aiart.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = aiart_client.AiartClient(cred, "ap-shanghai", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.TextToImageRequest()
        params = {
            "Prompt": prompt,
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个TextToImageResponse的实例，与请求对象对应
        resp = client.TextToImage(req)
        # 输出json格式的字符串回包
        # print(resp)
        res_json = json.loads(str(resp))

        img_data = base64.b64decode(res_json["ResultImage"])  # 解码时只要内容部分
        image = Image.open(BytesIO(img_data))
        output_path = Path(output).absolute().parent
        if not output_path.exists():
            os.makedirs(str(output_path))
        image.save(output)
    except TencentCloudSDKException as err:
        print(err)
