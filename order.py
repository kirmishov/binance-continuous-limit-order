import ccxt
from binance import Binance
import config
# import time
from datetime import datetime

# PLEASE CONFIGURE API DETAILS IN config.py

class LimitOrder():

    def __init__(self, market, price, type):
        self.binance = Binance(
            api_key=config.API_DETAILS['API_KEY'],
            api_secret=config.API_DETAILS['API_SECRET']
        )
        self.market = market
        self.price = price
        self.type = type
        self.running = False
        self.balance = self.binance.get_balance(self.market.split("/")[1])
        print ('Balance available: {} {}'.format(self.balance, self.market.split("/")[1]))

    def update(self):
        self.binance = Binance(
            api_key=config.API_DETAILS['API_KEY'],
            api_secret=config.API_DETAILS['API_SECRET']
        )
        try:
            if self.type == "sell":
                pass
            elif self.type == "buy":
                price = self.price
                amount = (self.balance / price) * 0.99 # maker/taker fee
                self.binance.buy(self.market, amount, price)
                print("Limit buy order placed | Price: %.8f" % (price))
                self.running = False


        except ccxt.InvalidOrder as e:
            print('ERROR: {}'.format(e))
        except ccxt.ExchangeError as e:
            # print('ERROR: {}'.format(e))
            print ("{} Market doesn't exist yet".format(datetime.now()), end="\r")


    def run(self):
        self.running = True
        while (self.running):
            self.update()
            # time.sleep(self.interval)
