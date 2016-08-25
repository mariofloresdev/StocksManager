from googlefinance import getQuotes
from yahoo_finance import Share
from datetime import date
from pprint import pprint
from datetime import timedelta
import urllib

class Company:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        try:
            self.share = Share(symbol)
            self.quotes = getQuotes(symbol)[0]
        except urllib.error.HTTPError:
            a = 2
    def __init__(self, symbol):
        self.name = symbol
        self.symbol = symbol
        try:
            self.share = Share(symbol)
            self.quotes = getQuotes(symbol)[0]
        except urllib.error.HTTPError:
            a = 2
               
        

    def refresh(self):
        self.share = Share(self.symbol)
        self.quotes = getQuotes(self.symbol)[0]

    def get_last_close(self):
        return self.share.get_prev_close()
    def get_price(self):
        self.refresh()
        return self.quotes["LastTradePrice"]
    def get_historical(self, start, end):
        return self.share.get_historical(start,end)
    
    def check_history(self, daysback):
        self.refresh()
        low = counter = high = close = 0
        historical = self.get_historical(str(date.today()-timedelta(int(daysback))), str(date.today()))
        #pprint(historical)
        print("Current Price", self.quotes["LastTradePrice"])
        higher = float(historical[0]["High"])
        higher_date = lower_date = historical[0]["Date"]
        lower = float(historical[0]["Low"])
        
        for h in historical:
            if (lower>float(h["Low"])):
                lower = float(h["Low"])
                lower_date = h["Date"]
            if (higher<float(h["High"])):
                higher = float(h["High"])
                higher_date = h["Date"]
            close+=float(h["Close"])
            low+=float(h["Low"])
            high+=float(h["High"])
            counter+=1
            
        self.closeAvg = float(int(1000*close/counter)/1000)
        
        self.lowAvg = float(int(1000*low/counter)/1000)
        self.lower = lower
        self.lowerDate = lower_date
        
        self.high_avg = float(int(1000*high/counter)/1000)
        self.higher = higher
        self.higher_date = higher_date
