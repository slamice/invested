class RobinHoodStock:
    def __init__(self, last_trade: dict):
        self.raw_stock_info = last_trade

    @property
    def code(self):
        return self.raw_stock_info.get('symbol')

    @property
    def adjusted_previous_close(self):
        return float(self.raw_stock_info.get('adjusted_previous_close'))

    @property
    def last_trade_price(self):
        return float(self.raw_stock_info.get('last_trade_price'))

    @property
    def bid_price(self):
        return float(self.raw_stock_info.get('bid_price'))

    @property
    def previous_close(self):
        return float(self.raw_stock_info.get('previous_close'))

    @property
    def buying_price(self):
        return float(self.raw_stock_info.get('bid_price'))

    def __str__(self):
        return '{} {}'.format(self.code, self.buying_price)
