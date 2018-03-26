from hightrademanager.hightrademanager import Account, StockActivityAudit, stock
from hightrademanager.hightrademanager import AverageCalculator
from hightrademanager.hightrademanager import CurrentStock
from hightrademanager.hightrademanager import BUY


class Buyer:
    def __init__(self, account: Account, current_stock: CurrentStock):
        self.account = account
        self.current_stock = current_stock
        self.average_calculator = AverageCalculator.create(current_stock=current_stock)

    def log_buy_audit(self):
        StockActivityAudit(stock__code=self.current_stock.code, activity=BUY)

    def buy(self):
        if self.current_stock.has_money_to_buy(stock) and self.average_calculator.has_average_volatility_or_lower():
            self.log_buy_audit()
        # TODO: buy in Robinhood