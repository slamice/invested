import os

from Robinhood import Robinhood
from apscheduler.schedulers.blocking import BlockingScheduler

from hightrademanager.models import Stock, StockPriceHistory
from hightrademanager.stocks.robinhood_stock import RobinHoodStock

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='8-20', minute='*/5')
def fetch_stocks():
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
