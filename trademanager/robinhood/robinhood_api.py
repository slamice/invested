import logging
import os

from Robinhood import Robinhood

from trademanager.models import Stock
from trademanager.stocks.robinhood_stock import RobinHoodStock

logger = logging.getLogger("invested_logs")


class RobinhoodAPI:
    def __init__(self):
        logger.info("logging into Robinhood...")
        robinhood_username = os.environ.get('ROBINHOOD_USERNAME')
        robinhood_password = os.environ.get('ROBINHOOD_PASSWORD')
        self._api = Robinhood()
        self._api.login(username=robinhood_username, password=robinhood_password)
        logger.info("logged in to Robinhood.")

    def get_stock_quote(self, stock: Stock) -> RobinHoodStock:
        robinhood_stock = None
        try:
            robinhood_stock = RobinHoodStock(last_trade=self._api.quote_data(stock.code))
        except Exception as e:
            logger.info("Error while fetching quote: {}".format(e))
        return robinhood_stock
