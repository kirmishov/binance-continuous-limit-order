# Binance Continuous Limit Order
Provides a continuous attempts to place limit order, e.g. for buying tokens at the start of market.
Works in buy mode only for now.


## Installation

**Install required libraries**
activate your virtualenv and then
```
pip install -r requirements.txt
```



## Configure API keys

Obtain an API key [here](https://www.binance.com/userCenter/createApi.html)

Then modify `config.py` and insert your API key and secret



## Running

**Usage**

```
$ python main.py --help
usage: main.py [-h] --symbol SYMBOL --price PRICE --type TYPE

optional arguments:
  -h, --help           show this help message and exit
  --symbol SYMBOL      Market Symbol (Ex: ONE/BTC - ONE/USDT)
  --price PRICE        Price in base coin (For Harmony (One) see:
                        https://wnbp.info/s/HarmonyToTheMoon)
  --type TYPE          Buying or selling mode. (Ex: 'buy' or 'sell')
```



**Important note**

Script will try to buy on your full available balance.
You can run several instances of script for different markets, e.g. ONE/BTC ONE/USDT ONE/BNB.
Trading levels for Harmony (ONE): https://wnbp.info/s/HarmonyToTheMoon
