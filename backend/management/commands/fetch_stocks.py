
import schedule
from django.core.management import BaseCommand

from backend.jobs.fetch_stocks import fetch_stocks


class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule.every(5).minutes.do(fetch_stocks())
