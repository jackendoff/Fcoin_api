from request_demo import get_data,post_data
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
        data = post_data(url, **headers)
        # print(data)
        return data

        pass

    def get_order_list(self,kwargs):
        '''
        查询订单列表
        :param kwargs:
        :return:
        '''

        url = 'https://api.fcoin.com/v2/orders'

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

    def get_one_order(self,order_id):
        url = 'https://api.fcoin.com/v2/orders/'+order_id

        nowtime = str(round(time.time() * 1000))
        auth = FcoinAuth(constant_dict['KEY'], constant_dict['SECRET KEY'], 'GET', url,
                         nowtime, POST_BODY=None)
        # 需要传入参数**kwargs
        url, headers = auth.get_signature()
        print(url)
        print(headers, type(headers))
        data = get_data(url, **headers)
        # print(data)
        return data
        pass

    def rollback_order(self,order_id):
        # 撤销订单
        url = 'https://api.fcoin.com/v2/orders/'+order_id+'/submit-cancel'
        nowtime = str(round(time.time() * 1000))
        auth = FcoinAuth(constant_dict['KEY'], constant_dict['SECRET KEY'], 'POST', url,
                         nowtime, POST_BODY=None)
        # 需要传入参数**kwargs
        url, headers = auth.get_signature()
        print(url)
        print(headers, type(headers))
        data = post_data(url, **headers)
        # print(data)
        return data

    def get_one_deal_data(self,order_id):
        #查询制定订单成交记录
        url = 'https://api.fcoin.com/v2/orders/' + order_id + '/match-results'
        nowtime = str(round(time.time() * 1000))
        auth = FcoinAuth(constant_dict['KEY'], constant_dict['SECRET KEY'], 'POST', url,
                         nowtime, POST_BODY=None)
        # 需要传入参数**kwargs
        url, headers = auth.get_signature()
        print(url)
        print(headers, type(headers))
        data = get_data(url, **headers)
        # print(data)
        return data
        pass


if __name__ == '__main__':
    kwargs = {
        'symbol': 'dageth',
        'states': 'submitted,partial_filled,partial_canceled',
        'before': '1544580502177',
        # 'after':'1544500000177',
        'limit': 20
    }
    customer = CustomerApi()
    data = customer.get_order_list(kwargs)
    print(data)