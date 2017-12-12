from django.db import models


class StockPriceHistory(models.Model):
    stock = models.ForeignKey('Stock', on_delete=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
