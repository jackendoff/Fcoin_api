from constant import constant_dict
import base64
import hmac
from hashlib import sha1
import time


class FcoinAuth(object):

    def __init__(self):
        pass

    def get_signature(self):
        '''
        获取签名
        :return:
        '''
        pass

    def request_data(self):
        '''
        使用签名和api—key发送请求
        :return:
        '''
        pass
