from constant import constant_dict
from request_demo import get_data
import base64
import hmac
from hashlib import sha1
import time


class FcoinAuth(object):

    def __init__(self,api_key,secret_key,HTTP_METHOD=None,HTTP_REQUEST_URI=None,TIMESTAMP=None,POST_BODY=None):
        self.api_key = api_key
        self.secret_key = secret_key
        self.HTTP_METHOD = HTTP_METHOD
        self.HTTP_REQUEST_URI = HTTP_REQUEST_URI
        self.TIMESTAMP = TIMESTAMP
        self.POST_BODY = POST_BODY

        pass

    def get_signature(self,**kwargs):
        '''需要传递参数
        HTTP_METHOD(大写) + HTTP_REQUEST_URI + TIMESTAMP + POST_BODY
        获取签名
        :return:signature
        '''
        if self.HTTP_METHOD == 'GET':
            # 拼接HTTP_REQUEST_URI
            # print(kwargs)
            # print(kwargs is None)
            if kwargs:
                self.HTTP_REQUEST_URI += '?'
            self.HTTP_REQUEST_URI += FcoinAuth.sort_dict_to_str(**kwargs)
            # 拼接字符串
            join_str = self.HTTP_METHOD+self.HTTP_REQUEST_URI+self.TIMESTAMP
            print(join_str)

            # 生成加密
            signature = str(base64.b64encode(join_str.encode("utf-8")), "utf-8")
            signature = hmac.new(self.secret_key.encode("utf-8"), signature.encode("UTF-8"),sha1).digest()
            signature = str(base64.b64encode(signature), "utf-8")
            url,headers = self.request_data(signature)

            return url,headers

            pass
        elif self.HTTP_METHOD == 'POST':
            # self.HTTP_REQUEST_URI += FcoinAuth.sort_dict_to_str(**kwargs)
            # 拼接字符串
            join_str = self.HTTP_METHOD+self.HTTP_REQUEST_URI+self.TIMESTAMP+self.sort_dict_to_str(**kwargs)
            print(join_str)

            # 生成加密
            signature = str(base64.b64encode(join_str.encode("utf-8")), "utf-8")
            signature = hmac.new(self.secret_key.encode("utf-8"), signature.encode("UTF-8"),sha1).digest()
            signature = str(base64.b64encode(signature), "utf-8")
            url,headers = self.request_data(signature)

            return url,headers
            pass
        elif self.HTTP_METHOD == 'DELETE':
            pass
        elif self.HTTP_METHOD == 'PUT':
            pass

        pass

    def request_data(self,signature):
        '''
        使用签名和api—key发送请求
        :return:
        '''
        headers = {}
        headers["FC-ACCESS-KEY"] = self.api_key
        headers["FC-ACCESS-SIGNATURE"] = signature
        headers["FC-ACCESS-TIMESTAMP"] = str(self.TIMESTAMP)
        # data = get_data(self.HTTP_REQUEST_URI,headers=headers)
        return self.HTTP_REQUEST_URI,headers

        pass

    @staticmethod
    def sort_dict_to_str(**dict_data):
        '''
        传入字典，按照key，排序连接为url字符串
        :return:
        '''
        key_list = sorted(dict_data.keys())
        dict_list = []
        for key_data in key_list:
            # print(key_data)
            data_str = key_data+'='+str(dict_data[key_data])
            dict_list.append(data_str)
        url_str = '&'.join(dict_list)
        return url_str


if __name__ == '__main__':
    kwargs = {
        'symbol':'dageth',
        'states':'submitted,partial_filled,partial_canceled',
        'before':'1544580502177',
        # 'after':'1544500000177',
        'limit':20
    }
    nowtime = str(round(time.time() * 1000))
    auth = FcoinAuth(constant_dict['KEY'],constant_dict['SECRET KEY'],'POST','https://api.fcoin.com/v2/orders',nowtime,POST_BODY=None)
    # 需要传入参数**kwargs
    signature = auth.get_signature(**kwargs)
    print(signature)