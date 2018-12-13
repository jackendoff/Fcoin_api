from request_demo import get_data

class PublicApi(object):
    '''
    获取公共接口数据
    '''
    def __init__(self,coin_name=None):
        '''
        :param coin_name:币对名字
        '''
        self.coin_name = coin_name
        pass

    def get_server_time(self):
        '''
        获取服务器时间
        :return:dict{状态码，时间戳}
        '''
        url = 'https://api.fcoin.com/v2/public/server-time'
        data = get_data(url)
        return data

    def get_all_coin_name(self):
        '''
        获取可用币种
        :return:dict{状态码，币种列表}
        '''
        url = 'https://api.fcoin.com/v2/public/currencies'
        data = get_data(url)
        return data

    def get_use_trading(self):
        '''
        查询交易所可用交易对
        :return:dict{status,data[{name,base,quote,}]}
        '''
        url = 'https://api.fcoin.com/v2/public/symbols'
        data = get_data(url)
        return data

    def get_ticker(self):
        '''
        行情 tick 信息, 包含最新成交价, 最新成交量, 买一卖一, 近 24 小时成交量
        :return:["最新成交价","最近一笔成交的成交量","最大买一价","最大买一量","最小卖一价","最小卖一量","24小时前成交价","24小时内最高价","24小时内最低价","24小时内基准货币成交量, 如 btcusdt 中 btc 的量","24小时内计价货币成交量, 如 btcusdt 中 usdt 的量"]
        '''
        url = 'https://api.fcoin.com/v2/market/ticker/'+self.coin_name
        data = get_data(url)
        return data

    def depth_data(self,level=None):
        '''
        获取深度列表
        :param level:深度级别（L20,L150,full）
        :return:tuple(bids_list_all, asks_list_all)
        '''
        if level is None:
            level = 'full'
        url = 'https://api.fcoin.com/v2/market/depth/'+level+'/'+self.coin_name
        depth_dict = get_data(url)
        bids_price_list = []
        bids_amount_list = []
        asks_price_list = []
        asks_amount_list = []
        try:
            bids_list = depth_dict['data']['bids']
            asks_list = depth_dict['data']['asks']
            n= 1
            for data in bids_list:
                if n%2 != 0:
                    bids_price_list.append(data)
                else:
                    bids_amount_list.append(data)
                n += 1
            n = 1
            for data in asks_list:
                if n%2 != 0:
                    asks_price_list.append(data)
                else:
                    asks_amount_list.append(data)
                n += 1

            bids_list_all = [bids_price_list,bids_amount_list]
            asks_list_all = [asks_price_list,asks_amount_list]
            return bids_list_all, asks_list_all
        except:
            print('depth_dice数据未获取到,可能是空字典')
        pass

    def get_trades_detail(self):
        '''
        获取最新成交明细
        :return:
        '''
        url = 'https://api.fcoin.com/v2/market/trades/'+self.coin_name
        data = get_data(url)
        return data

    def get_k_line(self, resolution=None):
        '''
        获取k线数据
        :param resolution: M1,M3,M5,,M15,M30,H1,H4,H6,D1,W1,MN
        :return: dict{status, data[{}]}
        '''
        if resolution is None:
            resolution = 'M1'
        url = 'https://api.fcoin.com/v2/market/candles/'+resolution+'/'+self.coin_name
        data = get_data(url)
        return data


if __name__ == '__main__':
    coin_name = 'dageth'
    coin = PublicApi(coin_name)
    data = coin.get_use_trading()
    print(data,type(data))
