#!/usr/bin/env python
# coding=utf-8

import os

# Flask settings
SECRET_KEY = os.environ.get('SECRET_KEY')
APP_URL = os.environ.get('APP_URL')

# Google keys
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
CUSTOM_SEARCH_ENGINE = os.environ.get('CUSTOM_SEARCH_ENGINE')

# Twitter Application Keys
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
CONSUMER_API_KEY = os.environ.get('CONSUMER_API_KEY')
CONSUMER_SECRET_KEY = os.environ.get('CONSUMER_SECRET_KEY')

# URL templates for apis
GOOGLE_URL_TEMPLATE = os.environ.get('GOOGLE_URL_TEMPLATE')
DDG_URL_TEMPLATE = os.environ.get('DDG_URL_TEMPLATE')
TWITTER_URL_TEMPLATE = os.environ.get('TWITTER_URL_TEMPLATE')
