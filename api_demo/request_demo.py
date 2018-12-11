import requests
import json
'''
请求url，获取数据，返回数据类型
'''


def get_data(url):
    data_re = requests.get(url)
    data = json.loads(data_re.content.decode())
    return data


if __name__ == '__main__':
    url = 'https://api.fcoin.com/v2/market/depth/full/dageth'
    data = get_data(url)
    print(data,type(data))