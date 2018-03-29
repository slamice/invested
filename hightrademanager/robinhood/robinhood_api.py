import os

from Robinhood import Robinhood

from hightrademanager.models import Stock
from hightrademanager.stocks.robinhood_stock import RobinHoodStock


class RobinhoodAPI:
    def __init__(self):
        robinhood_username = os.environ.get('ROBINHOOD_USERNAME')
        robinhood_password = os.environ.get('ROBINHOOD_PASSWORD')
        robinhood = Robinhood()
        self.robinhood_api = robinhood.login(username=robinhood_username, password=robinhood_password)

    def get_stock_quote(self, stock: Stock) -> RobinHoodStock:
        return RobinHoodStock(last_trade=self.robinhood_api.quote_data(stock.code))
