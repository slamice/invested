from datetime import datetime

from trademanager.models import Account, StockActivityAudit
from trademanager.stocks.constants import ROBINHOOD_DAILY_SELL_LIMIT


class CurrentStock:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    def has_money_to_buy(self, account: Account):
        return account.buying_power - self.price > account.limit

    def is_still_sellable_today(self):
        return StockActivityAudit.objects.get(created_at=datetime.today(),
                                              stock=self).count() < ROBINHOOD_DAILY_SELL_LIMIT
    def __lt__(self, other):
        return self.price < other
