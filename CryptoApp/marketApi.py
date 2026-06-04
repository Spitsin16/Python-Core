import requests
class MarketApi:
    def __init__(self):
        self.url = "https://api.rapira.net/open/market/rates"
        self.pairs = {}

    def get_market_api_pairs_from_rapira(self):
        message = (requests.get(self.url)).json()
        data = message['data']
        for pair in data:
            self.pairs[pair['symbol']] = {'buy': pair['askPrice'], 'sell': pair['bidPrice']}
        return self.pairs

    def show_pairs(self):
        active_coins = list(self.pairs.keys())
        print(*active_coins)

    def show_cources(self, operation):
        for item, value in self.pairs.items():
            print(item, value[operation])
