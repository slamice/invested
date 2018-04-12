import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from trademanager.models import Stock, StockPriceHistory
from trademanager.robinhood.robinhood_api import RobinhoodAPI

sched = BlockingScheduler()

logger = logging.getLogger("invested_logs")


class FetchStockManager:
    def fetch(self):
        robinhood_api = RobinhoodAPI()

        # Grab stocks from database
        stocks = Stock.objects.all()
        logger.info("Stocks available: {}".format(stocks))

        for stock in stocks:
            quote = robinhood_api.get_stock_quote(stock=stock)
            logger.info('{} {}'.format(quote.code, quote.buying_price))
            try:
                StockPriceHistory.objects.create(stock=stock, price=quote.buying_price)
            except Exception as e:
                logger.info('Major error going on here during adding stock history... {}'.format(e))
