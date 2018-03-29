from apscheduler.schedulers.blocking import BlockingScheduler

from hightrademanager.models import Stock, StockPriceHistory
from hightrademanager.robinhood.robinhood_api import RobinhoodAPI

sched = BlockingScheduler()


@sched.scheduled_job('cron', minute='*/5')
def fetch_stocks():
    robinhood_api = RobinhoodAPI()

    # Grab stocks from database
    stocks = Stock.objects.all()
    print(stocks)

    for stock in stocks:
        quote = robinhood_api.get_stock_quote(stock=stock)
        print('{} {}'.format(quote.code, quote.buying_price))
        StockPriceHistory.objects.create(stock=stock, price=quote.buying_price)
