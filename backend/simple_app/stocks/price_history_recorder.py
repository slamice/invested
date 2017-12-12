from decimal import Decimal

from backend.simple_app.models.stock_price_history import StockPriceHistory


class PriceHistoryRecorder:
    def __init__(self, stock_code: str):
        self.stock_code = stock_code

    def save_stock_history(self, price: Decimal):
        stock_price_history = StockPriceHistory(stock_id=self.stock_code, price=price)
        stock_price_history.save()
