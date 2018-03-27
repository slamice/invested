init: python manage.py db init
migrate: python manage.py db migrate
web: gunicorn hightrademanager.hightrademanager.wsgi:application --log-file -
fetch_stocks: python manage.py fetch_stocks