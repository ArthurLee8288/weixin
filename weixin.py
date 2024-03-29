# #encoding:utf-8
#
#
# from flask import Flask,url_for,redirect,render_template,request
# import hashlib
# import config
#
# app = Flask(__name__)



# -*- coding:utf-8 -*-

import config
from flask import Flask, request, make_response
import hashlib
# import xmltodict
import time

app = Flask(__name__)
app.config.from_object(config)

WECHAT_TOKEN = "logitech"


@app.route('/', methods=['GET', 'POST'])
def wechat():
    args = request.args


    signature = args.get('signature')
    timestamp = args.get('timestamp')
    nonce = args.get('nonce')
    echostr = args.get('echostr')
    print timestamp
    # 1. 将token、timestamp、nonce三个参数进行字典序排序
    temp = [WECHAT_TOKEN, timestamp, nonce]

    temp.sort()

    # 2. 将三个参数字符串拼接成一个字符串进行sha1加密
    temp = "".join([str(x) for x in temp])
    # sig是我们计算出来的签名结果
    sig = hashlib.sha1(temp).hexdigest()

    # 3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    if sig == signature:
        # 根据请求方式.返回不同的内容 ,如果是get方式,代表是验证服务器有效性
        # 如果POST方式,代表是微服务器转发给我们的消息
        if request.method == "GET":
            return echostr

    else:
        return 'errno', 403


if __name__ == '__main__':
    app.run()
