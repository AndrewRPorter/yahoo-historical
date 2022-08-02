import calendar as cal
import datetime as dt
import time
import pandas as pd
import requests
from io import StringIO
from .constants import API_URL, DATE_INTERVALS, ONE_DAY_INTERVAL


class Fetcher:
    def __init__(self, ticker, start, end=None, interval=ONE_DAY_INTERVAL):
        """Initializes class variables and formats api_url string"""
        self.ticker = ticker.upper()
        self.interval = interval
        self.start = int(cal.timegm(dt.datetime(*start).timetuple()))

        if end is not None:
            self.end = int(cal.timegm(dt.datetime(*end).timetuple()))
        else:
            self.end = int(time.time())

    def create_url(self, events):
        return API_URL % (self.ticker, self.start, self.end, self.interval, events)

    def _get(self, events, as_dataframe=True):
        if self.interval not in DATE_INTERVALS:
            raise ValueError(
                f"Incorrect interval: valid intervals are {', '.join(DATE_INTERVALS)}"
            )

        url = self.create_url(events)
        data = requests.get(url, headers={"User-agent": ""})
        content = StringIO(data.content.decode("utf-8"))

        dataframe = pd.read_csv(content, sep=",")
        if as_dataframe:
            return dataframe

        return dataframe.to_json()

    def get_historical(self, as_dataframe=True):
        """PEP8 friendly version of deprecated getHistorical function"""
        return self._get("history", as_dataframe=as_dataframe)

    def get_dividends(self, as_dataframe=True):
        """PEP8 friendly version of deprecated getDividends function"""
        return self._get("div", as_dataframe=as_dataframe)

    def get_splits(self, as_dataframe=True):
        """PEP8 friendly version of deprecated getSplits function"""
        return self._get("split", as_dataframe=as_dataframe)

    def get_date_price(self, as_dataframe=True):
        """PEP8 friendly version of deprecated getDatePrice function"""
        return self.get_historical(as_dataframe=as_dataframe).iloc[:, [0, 4]]

    def get_date_volume(self, as_dataframe=True):
        """PEP8 friendly version of deprecated getDateVolume function"""
        return self.get_historical(as_dataframe=as_dataframe).iloc[:, [0, 6]]
