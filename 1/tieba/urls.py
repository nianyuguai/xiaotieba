# coding=utf-8
__author__ = 'lixiaojian'

from django.conf.urls import patterns, url

from views import index

urlpatterns = patterns('',
                       url(r"^", index),
                       url(r"^login/$", "tieba.views.login",name="log"),
)