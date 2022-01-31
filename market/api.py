import json
from urllib.request import urlopen

# with urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cbeam%2CHelium%2Cuniswap%2Csushi%2Cstellar%2Ccardano%2Cpolkadot%2Cchainlink%2Ciota%2Celrond-erd-2%2CTezos%2CDogecoin%2C%2CDecentraland%2CChainLink%2CRipple%2CPolkadot%2CPancakeSwap%2CMIOTA%2Ctron%2cethereum-classic%2CCeler-Network%2CElrond-eGold%2CDusk-Network%2CPerlin%2Cpancakeswap-token%2Cbinancecoin&vs_currencies=usd&include_market_cap=true&include_24hr_change=true&include_last_updated_at=true") as response:
#     source = response.read()

with urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false") as response:
    source = response.read()

# data = json.loads(source)
data = json.loads(source)

# print (json.dumps(data, indent=2))

# print (data['bitcoin'])
# print (json.dumps(data2, indent=2))

# print (data2[0]['name'],data2[0]['current_price'])
#
# for i in range(len(data2)):
#     print (data2[i]['name'],data2[i]['current_price'], '$')
# print (len(data2))
