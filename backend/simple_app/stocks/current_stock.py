from datetime import datetime

from backend.simple_app.models.account import Account
from backend.simple_app.models.stock_activity_audit import StockActivityAudit
from backend.simple_app.stocks.constants import ROBINHOOD_DAILY_SELL_LIMIT


class CurrentStock:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    def has_money_to_buy(self, account: Account):
        return account.buying_power - self.price > account.limit

    def is_still_sellable_today(self):
        return StockActivityAudit.objects.get(created_at=datetime.today(),
                                              stock=self).count() < ROBINHOOD_DAILY_SELL_LIMIT
