import requests
import pandas as pd

class PseData:

    def __init__(self):
        self.base_url = "https://pselookup.vrymel.com/api/"
        self.open_stocks = self.all_open_stocks()

    def all_open_stocks(self):
        api_call = self.base_url + "stocks"
        response = requests.get(api_call)
        stocks_js = response.json()['stocks']

        open_stocks = []
        for i in stocks_js:
            if(i['status'] == "OPEN"):
                open_stocks.append(i['ticker_symbol'])
        return(open_stocks)

    def filter_rsi(self, lower_bound, upper_bound):
        open_stocks = self.open_stocks
        in_filter = {}
        for i in open_stocks:
            try:
                vals = PseStock(i).current_stock_info()
                rsi = float(vals['indicators']['rsi'])
                if(rsi > lower_bound and rsi < upper_bound):
                    in_filter[i] = rsi
            except:
                pass
        return(in_filter)

    def lookup_current_info(self, ticker):
        api_call = self.base_url + "stocks/{}".format(ticker)
        response = requests.get(api_call)
        ticker_js = response.json()
        rsi = ticker_js['indicators']['rsi']
        return(ticker_js)

    def lookup_historical_date(self, ticker, date):
        api_call = self.base_url + "/stocks/{}/history/{}".format(ticker, date)
        response = requests.get(api_call)
        ticker_js = response.json()
        ticker_js2 = ticker_js['history']
        # date, ticker, open, close, low, high, volume
        pod = [ticker_js2['trading_date'], ticker, ticker_js2['open'], ticker_js2['close'], ticker_js2['low'], ticker_js2['high'], ticker_js2['volume']]
        return(pod)

    def lookup_historical_range(self, ticker, start_date, end_date):
        api_call = self.base_url + "/stocks/{}/history/{}/{}".format(ticker, start_date, end_date)
        response = requests.get(api_call)
        range_js = response.json()['history']
        return(range_js)
