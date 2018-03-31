from django.db import models

from trademanager.stocks.types import ACTIVITY_TYPE


class StockActivityAudit(models.Model):
    stock = models.ForeignKey('Stock', on_delete=True)
    activity = models.CharField(default=None, null=True, max_length=50, choices=ACTIVITY_TYPE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.stock.name, self.activity, self.price, self.created_at)

    class Meta:
        db_table = 'stock_activity_audit'
