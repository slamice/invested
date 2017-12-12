# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . import models

admin.site.register(models.Account)
admin.site.register(models.Stock)
admin.site.register(models.StockActivityAudit)
admin.site.register(models.StockPriceHistory)