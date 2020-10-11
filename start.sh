#!/bin/sh



#! /bin/bash

#start second servvice here, and push it to background:
python manage.py qcluster &

#then run the last commands:
gunicorn tutorialSite.wsgi:application --workers=3 --bind 0.0.0.0:8080
