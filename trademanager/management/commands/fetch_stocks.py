from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import BaseCommand

from trademanager.stocks.fetch_stock_manager import FetchStockManager


class Command(BaseCommand):
    def handle(self, *args, **options):
        sched = BlockingScheduler()

        def fetch_stock():
            fetch_stock_manager = FetchStockManager()
            fetch_stock_manager.fetch()

        #sched.add_job(fetch_stock, 'cron', day_of_week='mon-fri', hour='8-20', minute='*/5')
        sched.add_job(fetch_stock, 'cron', day_of_week='mon-sun', minute='*/5')
        sched.start()
