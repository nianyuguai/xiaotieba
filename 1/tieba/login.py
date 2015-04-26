# coding=utf-8
__author__ = 'lixiaojian'

import sys
import weibo
import webbrowser

APP_KEY = '1829606972'
APP_SERCET = 'dadc3d2213fa3cd06a0b2c3315940676'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'

api = weibo.APIClient(app_key=APP_KEY, app_secret=APP_SERCET, redirect_uri=REDIRECT_URL)
authorize_url = api.get_authorize_url()
print authorize_url
webbrowser.open_new(authorize_url)

