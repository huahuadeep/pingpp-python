# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

# 设置 API Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
Transfer API 文档: https://www.pingxx.com/api#创建-transfer-对象
创建 Transfer 对象 - jdpay
'''
try:
    tr = pingpp.Transfer.create(
        # 付款使用的商户内部订单号: jdpay 限长1-64位不能重复的数字字母组合
        order_no=str_random(20),
        # 目前支持支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay，余额:balance
        channel='jdpay',
        # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100,企业付款最小发送金额为1 元）
        amount=100,
        # 三位 ISO 货币代码，目前仅支持人民币: cny 。
        currency='cny',
        app=dict(id='app_1Gqj58ynP0mHeX1q'),
        # 付款类型 (当前 alipay、wx_pub 仅支持: b2c,
        #     unionpay、allinpay、jdpay 支持:  b2b、b2c)
        type='b2c',
        extra=dict(
            # 必须，1~32位，收款人银行卡号或者存折号。
            card_number='6214888888888888',
            # 必须，1~100位，收款人姓名。
            user_name='张三',
            # 必须，4位，开户银行编号，详情请参考 企业付款（银行卡）银行编号说明：
            #     https://www.pingxx.com/api#银行编号说明
            open_bank_code='0103'
        ),
        description='description'
    )
    print(tr.to_str())  # 输出 Ping++ 返回的企业付款对象 Transfer
except Exception as e:
    raise
