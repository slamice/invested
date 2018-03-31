import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from trademanager.models import Stock, StockPriceHistory
from trademanager.robinhood.robinhood_api import RobinhoodAPI

sched = BlockingScheduler()

logger = logging.getLogger(__name__)

#@sched.scheduled_job('cron', minute='*/5',day_of_week='mon-fri')

class FetchStockManager:
    def start_job(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.fetch_stocks,
                          trigger='cron',
                          minute='*/5',
                          hour='8-20',
                          day_of_week='mon-fri')
        scheduler.start()

    def fetch_stocks(self):
        robinhood_api = RobinhoodAPI()

        # Grab stocks from database
        stocks = Stock.objects.all()
        logger.info("Stocks available: {}".format(stocks))

        for stock in stocks:
            quote = robinhood_api.get_stock_quote(stock=stock)
            logger.info('{} {}'.format(quote.code, quote.buying_price))
            StockPriceHistory.objects.create(stock=stock, price=quote.buying_price)
