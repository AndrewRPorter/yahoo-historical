import datetime as dt
import pandas as pd
import requests
import re
import csv

class Fetcher:
    def __init__(self, ticker, start, *args):
        self.ticker = ticker.upper()
        self.cookie, self.crumb = self.init()

        self.start = int(dt.datetime(start[0],start[1],start[2]).timestamp())

        if args:
            end = args[0]
            self.end = int(dt.datetime(end[0],end[1],end[2]).timestamp())
        else:
            self.end = str(int(dt.datetime.now()))

    def init(self):
        """Returns a tuple pair of cookie and crumb used in the request"""
        url = 'https://finance.yahoo.com/quote/%s/history' % (self.ticker)
        r = requests.get(url)
        txt = r.content
        cookie = r.cookies['B']
        pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')

        for line in txt.splitlines():
            m = pattern.match(line.decode("utf-8"))
            if m is not None:
                crumb = m.groupdict()['crumb']
        return cookie, crumb  # return a tuple of crumb and cookie

    def getHistorical(self):
        """Returns a list of historical data from Yahoo Finance"""
        url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&crumb=%s" % (self.ticker, self.start, self.end, self.crumb)
        data = requests.get(url, cookies={'B':self.cookie})
        content = data.content.decode("utf-8")
        csv_content = csv.reader(content.splitlines(), delimiter=',')
        return pd.DataFrame(list(csv_content))

    def getDatePrice(self):
        """Returns a DataFrame for Date and Price from getHistorical()"""
        return self.getHistorical().ix[0:,5]

    def getDateVolume(self):
        """Returns a DataFrame for Date and Volume from getHistorical()"""
        return self.getHistorical().ix[0:,6]

"""
Creates a Pandas DataFrame object storing all data
['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
"""
fetch = Fetcher("AAPL", [2007,1,1], [2017,1,1])

print(fetch.getHistorical())
print(fetch.getDatePrice())
print(fetch.getDateVolume())
