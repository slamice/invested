
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import BaseCommand

from hightrademanager.hightrademanager.fetch_stocks import fetch_stocks


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            scheduler = BackgroundScheduler()
            scheduler.add_job(fetch_stocks,
                              trigger='cron',
                              minute='*/5',
                              day_of_week='mon-fri',
                              hour='8-20')

            scheduler.start()
        except Exception as e:
            print(e)