from typing import Union
import time
import calendar as cal
import datetime as dt
import pandas as pd
import requests
from io import StringIO
from .constants import API_URL, DATE_INTERVALS, ONE_DAY_INTERVAL

def conv_df(resp):
    j = resp.json()
    
    # Extract the data explicitly by field name
    timestamps = j['chart']['result'][0]['timestamp']
    indicators = j['chart']['result'][0]['indicators']['quote'][0]
    adj = j['chart']['result'][0]['indicators']['adjclose'][0]
    
    # Explicitly extract each field by its key to avoid any mismatch
    close = indicators.get('close', [])
    open_ = indicators.get('open', [])
    high = indicators.get('high', [])
    low = indicators.get('low', [])
    adjclose = adj.get('adjclose', [])
    volume = indicators.get('volume', [])

    # Create the DataFrame with the correct order of columns
    df = pd.DataFrame({
        'timestamp': timestamps,
        'Open': open_,
        'High': high,
        'Low': low,
        'Close': close,
        'Adj Close': adjclose,
        'Volume': volume
    })
    
    # Add datetime columns
    df['time'] = pd.to_datetime(df['timestamp'], unit='s')
    df['Date'] = df['time'].apply(lambda x: x.strftime('%Y-%m-%d'))
    del df['time']
    del df['timestamp']
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]
    return df

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

        data = requests.get(url, headers={"User-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)"})

        dataframe = conv_df(data)
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
