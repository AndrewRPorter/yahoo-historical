import datetime as dt
import requests
import re
import time
import csv
# search with regular expressions

# "CrumbStore":\{"crumb":"(?<crumb>[^"]+)"\}

url = 'https://finance.yahoo.com/quote/AAPL/history' # url for a ticker symbol, with a download link
r = requests.get(url)  # download page

txt = r.text # extract html


cookie = r.cookies['B'] # the cooke we're looking for is named 'B'
print('Cookie: ', cookie)

# Now we need to extract the token from html.
# the string we need looks like this: "CrumbStore":{"crumb":"lQHxbbYOBCq"}
# regular expressions will do the trick!

pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')

for line in txt.splitlines():
    m = pattern.match(line)
    if m is not None:
        crumb = m.groupdict()['crumb']


print('Crumb=',crumb)
start = str(int(dt.datetime(2007,1,1).timestamp()))
end = str(int(time.time()))
ticker = "GEVO"
ticker = ticker.upper()

#or int(time.time()) for current timestamp
url = "https://query1.finance.yahoo.com/v7/finance/download/" + ticker + "?period1=" + start + "&period2=" + end + "&interval=1d&events=history&crumb=" + crumb
data = requests.get(url, cookies={'B':cookie})
content = data.content.decode("utf-8")
csv_content = csv.reader(content.splitlines(), delimiter=',')


#['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
for row in list(csv_content):
    if len(row) == 7:  # only get correctly formatted rows
        print(row)
