from typing import Union
import time
import pandas as pd
import requests
from io import StringIO
from .constants import API_URL, DATE_INTERVALS, ONE_DAY_INTERVAL


class Fetcher:
    def __init__(
        self,
        ticker: str,
        start: Union[int, float],
        end: Union[int, float] = time.time(),
        interval: str = ONE_DAY_INTERVAL,
    ):
        self.ticker = ticker.upper()
        self.interval = interval

        # we convert the unix timestamps to int here to avoid sending floats to yahoo finance API
        # as the API will reject the call for an invalid type
        self.start = int(start)
        self.end = int(end)

    def create_url(self, event: str) -> str:
        """Generate a URL for a particular event.

        Args:
            event (str): event type to query for ('history', 'div', 'split')

        Returns:
            str: formatted URL for an API call
        """
        return API_URL % (self.ticker, self.start, self.end, self.interval, event)

    def _get(self, event: str, as_dataframe=True) -> Union[pd.DataFrame, dict]:
        """Private helper function to build URL and make API request to grab data

        Args:
            event (str): kind of data we want to query (history, div, split)
            as_dataframe (bool, optional): whether or not to return data as a pandas DataFrame. Defaults to True.

        Raises:
            ValueError: if invalid interval is supplied

        Returns:
            Union[pd.DataFrame, dict]: data from yahoo finance API call
        """
        if self.interval not in DATE_INTERVALS:
            raise ValueError(
                f"Incorrect interval: valid intervals are {', '.join(DATE_INTERVALS)}"
            )

        url = self.create_url(event)
        # yahoo finance rejects our API request without an empty user agent
        data = requests.get(url, headers={"User-agent": ""})
        content = StringIO(data.content.decode("utf-8"))

        dataframe = pd.read_csv(content, sep=",")
        if as_dataframe:
            return dataframe

        return dataframe.to_json()

    def get_historical(self, as_dataframe=True):
        """Returns a list of historical price data from Yahoo Finance"""
        return self._get("history", as_dataframe=as_dataframe)

    def get_dividends(self, as_dataframe=True):
        """Returns a list of historical dividends data from Yahoo Finance"""
        return self._get("div", as_dataframe=as_dataframe)

    def get_splits(self, as_dataframe=True):
        """Returns a list of historical stock splits from Yahoo Finance"""
        return self._get("split", as_dataframe=as_dataframe)
