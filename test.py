from yahoo_historical import Fetcher

f = Fetcher("AAPL", [1960, 1, 1])
print(f.getHistorical())
