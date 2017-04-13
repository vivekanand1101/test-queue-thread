#!/usr/bin/env python
# coding=utf-8

import time

import requests

url = 'http://localhost:5000/?q=the+dark+knight'

start = time.time()
response = requests.get(url)
end = time.time()
print end - start
print response.status_code
