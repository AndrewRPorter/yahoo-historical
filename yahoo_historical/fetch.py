import calendar as cal
import datetime as dt
import re
import time
import warnings

import pandas as pd
import requests

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


class Fetcher:
    api_url = (
        "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=%s&events=%s&crumb=%s"
    )

    def __init__(self, ticker, start, end=None, interval="1d"):
        """Initializes class variables and formats api_url string"""
        self.ticker = ticker.upper()
        self.interval = interval
        self.cookie, self.crumb = self.init()
        self.start = int(cal.timegm(dt.datetime(*start).timetuple()))

        if end is not None:
            self.end = int(cal.timegm(dt.datetime(*end).timetuple()))
        else:
            self.end = int(time.time())

    def init(self):
        """Returns a tuple pair of cookie and crumb used in the request"""
        url = "https://finance.yahoo.com/quote/%s/history" % (self.ticker)
        r = requests.get(url)
        txt = r.content
        cookie = r.cookies["B"]
        pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')

        for line in txt.splitlines():
            m = pattern.match(line.decode("utf-8"))
            if m is not None:
                crumb = m.groupdict()["crumb"]
                crumb = crumb.replace(u"\\u002F", "/")
        return cookie, crumb  # return a tuple of crumb and cookie

    def _get(self, events):
        if self.interval not in ["1d", "1wk", "1mo"]:
            raise ValueError("Incorrect interval: valid intervals are 1d, 1wk, 1mo")

        url = self.api_url % (self.ticker, self.start, self.end, self.interval, events, self.crumb)

        data = requests.get(url, cookies={"B": self.cookie})
        content = StringIO(data.content.decode("utf-8"))
        return pd.read_csv(content, sep=",")

    def getData(self, events):
        """Returns a list of historical data from Yahoo Finance"""
        warnings.warn("getData has been deprecated, use get_data instead", DeprecationWarning)
        return self._get(events)

    def getHistorical(self):
        """Returns a list of historical price data from Yahoo Finance"""
        warnings.warn("getHistorical has been deprecated, use get_historical instead", DeprecationWarning)
        return self._get("history")

    def getDividends(self):
        """Returns a list of historical dividends data from Yahoo Finance"""
        warnings.warn("getDividends has been deprecated, use get_dividends instead", DeprecationWarning)
        return self._get("div")

    def getSplits(self):
        """Returns a list of historical splits data from Yahoo Finance"""
        warnings.warn("getSplits has been deprecated, use get_splits instead", DeprecationWarning)
        return self._get("split")

    def getDatePrice(self):
        """Returns a DataFrame for Date and Price from getHistorical()"""
        warnings.warn("getDatePrice has been deprecated, use get_date_price instead", DeprecationWarning)
        return self.getHistorical().iloc[:, [0, 4]]

    def getDateVolume(self):
        """Returns a DataFrame for Date and Volume from getHistorical()"""
        warnings.warn("getDateVolume has been deprecated, use get_date_volume instead", DeprecationWarning)
        return self.getHistorical().iloc[:, [0, 6]]

    def get_historical(self):
        """PEP8 friendly version of deprecated getHistorical function"""
        return self._get("history")

    def get_dividends(self):
        """PEP8 friendly version of deprecated getDividends function"""
        return self._get("div")

    def get_splits(self):
        """PEP8 friendly version of deprecated getSplits function"""
        return self._get("split")

    def get_date_price(self):
        """PEP8 friendly version of deprecated getDatePrice function"""
        return self.get_historical().iloc[:, [0, 4]]

    def get_date_volume(self):
        """PEP8 friendly version of deprecated getDateVolume function"""
        return self.get_historical().iloc[:, [0, 6]]
