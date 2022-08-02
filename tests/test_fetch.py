from yahoo_historical import Fetcher
import datetime
import time

TEST_TICKER = "AAPL"
TIME_START = time.mktime(datetime.datetime(2007, 1, 1).timetuple())
TIME_END = time.mktime(datetime.datetime(2017, 1, 1).timetuple())


def test_get_no_dataframe():
    data = Fetcher(TEST_TICKER, TIME_START, TIME_END).get_historical(as_dataframe=False)
    assert len(data) > 0


def test_get_with_lowercase():
    data = Fetcher(TEST_TICKER.lower(), TIME_START, TIME_END).get_historical()
    assert len(data) > 0


def test_get_historical():
    data = Fetcher(TEST_TICKER, TIME_START, TIME_END).get_historical()
    assert len(data) > 0


def test_get_dividends():
    data = Fetcher(TEST_TICKER, TIME_START, TIME_END).get_dividends()
    assert len(data) > 0


def test_get_splits():
    data = Fetcher(TEST_TICKER, TIME_START, TIME_END).get_splits()
    assert len(data) > 0


def test_get_date_price():
    data = Fetcher(TEST_TICKER, TIME_START, TIME_END).get_date_price()
    assert len(data) > 0


def test_get_date_volume():
    data = Fetcher(TEST_TICKER, TIME_START, TIME_END).get_date_volume()
    assert len(data) > 0
