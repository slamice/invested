from django.core.management import base

from trademanager.stocks.fetch_stocks import FetchStockManager


class Command(base.BaseCommand):
    def handle(self, *args, **options):
        manager = FetchStockManager()
        manager.start_job()
