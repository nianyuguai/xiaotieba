from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
import django


def home(request):
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT
    return HttpResponse("Hello,  django! version: " + str(django.VERSION) ＋ "user: " +
    MYSQL_USER + "password" + MYSQL_PASS)
