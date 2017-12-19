from Robinhood import Robinhood

from backend import Stock, StockPriceHistory


def fetch_stocks(trader: Robinhood):
    # Grab stocks from database
    stocks = Stock.objects.all()
    for stock in stocks:
        quote = trader.quote_data(stock.code)
        StockPriceHistory.objects.create(stock=stock, price=quote.price)

