import json
from urllib.request import urlopen

with urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page"
             "=1&sparkline=false") as response:
    source = response.read()

data = json.loads(source)
