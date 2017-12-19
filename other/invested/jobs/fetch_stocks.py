import schedule
from Robinhood import Robinhood

from django.core.management import BaseCommand

from backend import fetch_stocks


class Command(BaseCommand):
    def handle(self, *args, **options):
        trader = Robinhood()
        logged_in = trader.login(username="slamice", password="1sobigar")
        schedule.every(5).minutes.do(fetch_stocks(trader=trader))
