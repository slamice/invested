from decimal import Decimal

from trademanager.models import StockPriceHistory


class PriceHistoryRecorder:
    def __init__(self, stock_code: str):
        self.stock_code = stock_code

    def save_stock_history(self, price: Decimal) -> None:
        StockPriceHistory.objects.create(stock_id=self.stock_code, price=price)
