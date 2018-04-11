import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from trademanager.models import Stock, StockPriceHistory
from trademanager.robinhood.robinhood_api import RobinhoodAPI

sched = BlockingScheduler()

logger = logging.getLogger(__name__)


class FetchStockManager:
    def fetch(self):
        robinhood_api = RobinhoodAPI()

        # Grab stocks from database
        stocks = Stock.objects.all()
        logger.info("Stocks available: {}".format(stocks))

        for stock in stocks:
            quote = robinhood_api.get_stock_quote(stock=stock)
            logger.info('{} {}'.format(quote.code, quote.buying_price))
            StockPriceHistory.objects.create(stock=stock, price=quote.buying_price)
