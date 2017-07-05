import datetime as dt
import requests
import re
import time
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
start = dt.datetime(2007,1,1).timestamp()
end = dt.datetime(2007,1,1).timestamp()
#or int(time.time()) for current timestamp
url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1467662202&period2=1499198202&interval=1d&events=history&crumb=" + crumb
data = requests.get(url, cookies={'B':cookie})
#data = data.text

for line in data:
    print(line.decode("utf-8"))
    print()

#use this for printing csv
#https://stackoverflow.com/questions/35371043/use-python-requests-to-download-csv
