import os

from Robinhood import Robinhood

from backend.models import Stock, StockPriceHistory
from backend.stocks.robinhood_stock import RobinHoodStock


def fetch_stocks():
    import pdb; pdb.set_trace()
    robinhood_username = os.environ.get('ROBINHOOD_USERNAME')
    robinhood_password = os.environ.get('ROBINHOOD_PASSWORD')
    trader = Robinhood()

    logged_in = trader.login(username=robinhood_username,
                             password=robinhood_password)

    # Grab stocks from database
    stocks = Stock.objects.all()
    print(stocks)
    for stock in stocks:
        quote = RobinHoodStock(last_trade=trader.quote_data(stock.code))
        print('{} {}'.format(quote.code, quote.buying_price))
        StockPriceHistory.objects.create(stock=stock, price=quote.buying_price)
