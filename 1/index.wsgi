#coding=utf-8
import sae

from web import wsgi


application = sae.create_wsgi_app(wsgi.application)