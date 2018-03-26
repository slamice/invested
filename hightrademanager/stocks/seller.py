from hightrademanager.hightrademanager import Account, StockActivityAudit
from hightrademanager.hightrademanager import AverageCalculator
from hightrademanager.hightrademanager import CurrentStock
from hightrademanager.hightrademanager import SELL


class Seller:
    def __init__(self, account: Account, current_stock: CurrentStock):
        self.account = account
        self.current_stock = current_stock
        self.average_calculator = AverageCalculator.create(current_stock=current_stock)

    def log_sell_audit(self):
        StockActivityAudit(stock__code=self.current_stock.code, activity=SELL)

    def sell(self, stock):
        if self.current_stock.is_still_sellable_today() and self.average_calculator.has_average_volatility_or_higher():
            # Test sell
            self.log_sell_audit()
            # TODO: sell in Robinhood, keep checking until it's sold