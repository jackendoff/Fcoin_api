from request_demo import get_data
from constant_data import constant_dict


class CustomerApi(object):
    '''
    获取私有接口数据
    '''
    def get_balance_data(self):
        url = 'GET https://api.fcoin.com/v2/accounts/balance'
        data = get_data(url)
        return data
    

if __name__ == '__main__':
    customer = CustomerApi()
    data = customer.get_balance_data()
    print(data)