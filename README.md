[![PyPi version](https://badge.fury.io/py/yahoo-historical.svg)](https://badge.fury.io/py/yahoo-historical) [![Total downloads via Pip](https://pepy.tech/badge/yahoo-historical)](https://pepy.tech/project/yahoo_historical) [![yahoo-historical build status](https://circleci.com/gh/AndrewRPorter/yahoo-historical.svg?style=svg)](https://app.circleci.com/pipelines/github/AndrewRPorter/yahoo-historical)

# yahoo-historical

## Installation

```
pip install --user yahoo-historical
```

## Methods

- get_historical()
- get_dividends()
- get_splits()
- get_date_price()
- get_date_volume()

## Example Usage

Below details the available method params for creating a Fetcher object.

### Arguments

- ticker: The ticker symbol to download historical data for
- start: Start date as Unix timestamp

### Optional Arguments

- end: End date as Unix timestamp
- interval: Interval to fetch historical data (can be 1d, 1wk, 1mo, defaults to 1d)

```python
from yahoo_historical import Fetcher
import datetime
import time

# create unix timestamp representing January 1st, 2007
timestamp = time.mktime(datetime.datetime(2007, 1, 1).timetuple())

data = Fetcher("AAPL", timestamp)
print(data.get_historical())
```

```
                Date        Open        High         Low       Close   Adj Close      Volume
    0     2007-01-03   12.327143   12.368571   11.700000   10.812462   11.971429   309579900
    1     2007-01-04   12.007143   12.278571   11.974286   11.052453   12.237143   211815100
    2     2007-01-05   12.252857   12.314285   12.057143   10.973743   12.150000   208685400
    3     2007-01-08   12.280000   12.361428   12.182858   11.027935   12.210000   199276700
```

Note that you can return a dictionary instead of a DataFrame by setting the `as_dataframe` flag to `False`.

```python
from yahoo_historical import Fetcher

import datetime
import time

# create unix timestamp representing January 1st, 2007
timestamp = time.mktime(datetime.datetime(2007, 1, 1).timetuple())

data = Fetcher("AAPL", timestamp)
print(data.get_historical(as_dataframe=False))
```
