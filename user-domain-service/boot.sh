#!/bin/sh
source pipenv shell
flask db upgrade
flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - app_service:app
