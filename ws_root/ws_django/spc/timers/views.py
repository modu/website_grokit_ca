
import os
import glob
import codecs

from django.http import HttpResponse

def index(request, param):
    fh = open('./ws_django/spc/timers/index.html', 'r')
    html = fh.read()
    fh.close()

    return HttpResponse(html)

