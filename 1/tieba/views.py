from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template

from django.template import RequestContext


def index(request):

    c = RequestContext(request, {'foo': 'bar'})
    t = get_template('index.html')
    return HttpResponse(t.render(c))


def login(request):

    print "login..."
    c = RequestContext(request, {'foo': 'bar'})
    t = get_template('index.html')
    return HttpResponse(t.render(c))


