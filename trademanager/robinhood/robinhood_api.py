import logging
import os

from Robinhood import Robinhood

from trademanager.models import Stock
from trademanager.stocks.robinhood_stock import RobinHoodStock

logger = logging.getLogger(__name__)


class RobinhoodAPI:
    def __init__(self):
        logger.info("logging into Robinhood...")
        robinhood_username = os.environ.get('ROBINHOOD_USERNAME')
        robinhood_password = os.environ.get('ROBINHOOD_PASSWORD')
        self._api = Robinhood()
        self._api.login(username=robinhood_username, password=robinhood_password)
        logger.info("logged in to Robinhood.")

    def get_stock_quote(self, stock: Stock) -> RobinHoodStock:
        return RobinHoodStock(last_trade=self._api.quote_data(stock.code))