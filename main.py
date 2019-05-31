from order import LimitOrder
import argparse

def main(options):

    if options.type not in ['buy', 'sell']:
        print("Error: Please use valid trail type (Ex: 'buy' or 'sell')")
        return
    
    task = LimitOrder(options.symbol, options.price, options.type)
    task.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', type=str, help='Market Symbol (Ex: ONE/BTC - ONE/USDT)', required=True)
    parser.add_argument('--price', type=float, help='Price limit order (Ex: https://wnbp.info/s/HarmonyToTheMoon)', required=True)
    parser.add_argument('--type', type=str, help="Specify buy or sell limit order. (Ex: 'buy' or 'sell')", required=True)

    options = parser.parse_args()
    main(options)
