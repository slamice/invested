from django.db import models


class Account(models.Model):
    user = models.ForeignKey('auth.User', on_delete=True)
    portfolio_value = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    buying_power = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    limit = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'account'
