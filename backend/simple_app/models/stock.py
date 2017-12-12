from django.db import models

from ..stocks.types import VOLATILITY_TYPES


class Stock(models.Model):
    code = models.CharField(max_length=6, unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=100)
    volatility = models.CharField(default=None, null=True, max_length=50, choices=VOLATILITY_TYPES)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
