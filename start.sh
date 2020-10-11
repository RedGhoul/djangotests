#! /bin/bash

#start second servvice here, and push it to background:
gunicorn tutorialSite.wsgi:application --workers=3 --bind 0.0.0.0:8080 &

python manage.py qcluster 
