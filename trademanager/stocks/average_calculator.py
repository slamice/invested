from statistics import mean

from trademanager.models import StockPriceHistory
from trademanager.stocks.constants import STOCK_RECORDS_FOR_AVERAGE
from trademanager.stocks.current_stock import CurrentStock


class AverageCalculator:
    def __init__(self, current_stock: CurrentStock, min_price: float, average: float):
        self.min_price = min_price
        self.average = average
        self.difference = average - min_price
        self.current_stock = current_stock

    @staticmethod
    def get_last_stock_prices(current_stock):
        return StockPriceHistory.objects\
            .filter(stock__code=current_stock.code)\
            .order_by('-created_at').values('price', flat=True)[STOCK_RECORDS_FOR_AVERAGE]

    @staticmethod
    def create(current_stock: CurrentStock):
        prices = AverageCalculator.get_last_stock_prices(current_stock)
        return AverageCalculator(min_price=min(prices),
                                 average=mean(prices),
                                 current_stock=current_stock)

    def has_average_volatility_or_higher(self):
        """
        :return: True if current_stock has greater than the average price, else False
        """
        return self.current_stock > self.min_price + self.difference

    def has_average_volatility_or_lower(self):
        return self.current_stock < self.min_price - self.difference
