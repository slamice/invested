init: python manage.py db init
migrate: python manage.py db migrate
web: gunicorn --pythonpath hightrademanager.hightrademanager.wsgi:application --log-file -
fetch_stocks: python hightrademanager/hightrademanager/fetch_stocks.py