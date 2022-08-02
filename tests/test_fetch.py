from yahoo_historical import Fetcher

TEST_TICKER = "AAPL"


def test_get_no_dataframe():
    data = Fetcher("AAPL", [2007, 1, 1], [2017, 1, 1]).get_historical(
        as_dataframe=False
    )
    assert len(data) > 0


def test_get_with_lowercase():
    data = Fetcher("aapl", [2007, 1, 1], [2017, 1, 1]).get_historical()
    assert len(data) > 0


def test_get_historical():
    data = Fetcher(TEST_TICKER, [2007, 1, 1], [2017, 1, 1]).get_historical()
    assert len(data) > 0


def test_get_dividends():
    data = Fetcher(TEST_TICKER, [2007, 1, 1], [2017, 1, 1]).get_dividends()
    assert len(data) > 0


def test_get_splits():
    data = Fetcher(TEST_TICKER, [2007, 1, 1], [2017, 1, 1]).get_splits()
    assert len(data) > 0


def test_get_date_price():
    data = Fetcher(TEST_TICKER, [2007, 1, 1], [2017, 1, 1]).get_date_price()
    assert len(data) > 0


def test_get_date_volume():
    data = Fetcher(TEST_TICKER, [2007, 1, 1], [2017, 1, 1]).get_date_volume()
    assert len(data) > 0
