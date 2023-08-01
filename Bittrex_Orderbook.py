import pandas as pd
import requests


orderbook = requests.get('https://api.bittrex.com/v3/markets/DFI-BTC/orderbook').json()

# If you want separate data frames
bids = pd.DataFrame(orderbook['bid'])
asks = pd.DataFrame(orderbook['ask'])

# You can also merge the two into one
df = pd.merge(bids, asks, left_index=True, right_index=True)
df = df.rename({"rate_x":"Bid Price","quantity_x":"Bid Amount",
                "rate_y":"Ask Price","quantity_y":"Ask Amount"}, axis='columns')
df.head()

print(asks)