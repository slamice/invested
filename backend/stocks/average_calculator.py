from statistics import mean

from backend.models import StockPriceHistory
from backend.stocks.constants import STOCK_RECORDS_FOR_AVERAGE
from backend.stocks.current_stock import CurrentStock


class AverageCalculator:
    def __init__(self, current_stock: CurrentStock, min_price: float, average: float, difference: float):
        self.min_price = min_price
        self.average = average
        self.difference = difference
        self.current_stock = current_stock

    def create(current_stock: CurrentStock):
        prices = StockPriceHistory.objects\
            .filter(stock__code=current_stock.code)\
            .order_by('-created_at').values('price', flat=True)[STOCK_RECORDS_FOR_AVERAGE]
        min_price = min(prices)
        average = mean(prices)
        difference = average - min_price
        return AverageCalculator(min_price=min_price,
                                 average=average,
                                 difference=difference,
                                 current_stock=current_stock)

    def has_average_volatility_or_higher(self):
        """
        :return: True if current_stock has greater than the average price, else False
        """
        return self.current_stock.price > self.min_price + self.difference

    def has_average_volatility_or_lower(self):
        return self.current_stock.price < self.min_price - self.difference
