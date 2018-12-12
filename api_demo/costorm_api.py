from request_demo import get_data
from login import FcoinAuth
from constant import constant_dict
import time


class CustomerApi(object):
    '''
    获取私有接口数据
    不能使用，未找到原因
    '''
    def get_balance_data(self):
        url = 'https://api.fcoin.com/v2/accounts/balanc'
        # kwargs = {
        #     'symbol': 'dageth',
        #     'states': 'submitted,partial_filled,partial_canceled',
        #     'before': '1544580502177',
        #     # 'after':'1544500000177',
        #     'limit': 20
        # }
        nowtime = str(round(time.time() * 1000))
        auth = FcoinAuth(constant_dict['KEY'], constant_dict['SECRET KEY'], 'GET', url,
                         nowtime, POST_BODY=None)
        # 需要传入参数**kwargs
        url, headers = auth.get_signature()
        print(url)
        print(headers,type(headers))
        data = get_data(url,**headers)
        # print(data)
        return data

    def create_new_order(self):

        url = 'https://api.fcoin.com/v2/orders'
        kwargs = {
            'symbol': 'dageth',
            'states': 'submitted,partial_filled,partial_canceled',
            'before': '1544580502177',
            # 'after':'1544500000177',
            'limit': 20
        }
        nowtime = str(round(time.time() * 1000))
        auth = FcoinAuth(constant_dict['KEY'], constant_dict['SECRET KEY'], 'POST', url,
                         nowtime, POST_BODY=None)
        # 需要传入参数**kwargs
        url, headers = auth.get_signature(**kwargs)
        print(url)
        print(headers, type(headers))
        data = get_data(url, **headers)
        # print(data)
        return data

        pass

    def get_order_list(self):

        url = 'https://api.fcoin.com/v2/orders'
        kwargs = {
            'symbol': 'dageth',
            'states': 'submitted,partial_filled,partial_canceled',
            'before': '1544580502177',
            # 'after':'1544500000177',
            'limit': 20
        }
        nowtime = str(round(time.time() * 1000))
        auth = FcoinAuth(constant_dict['KEY'], constant_dict['SECRET KEY'], 'GET', url,
                         nowtime, POST_BODY=None)
        # 需要传入参数**kwargs
        url, headers = auth.get_signature(**kwargs)
        print(url)
        print(headers, type(headers))
        data = get_data(url, **headers)
        # print(data)
        return data
        pass

    def get_one_order(self):
        pass

    def rollback_order(self):
        pass

    def get_one_deal_data(self):
        pass


if __name__ == '__main__':
    customer = CustomerApi()
    data = customer.get_order_list()
    print(data)