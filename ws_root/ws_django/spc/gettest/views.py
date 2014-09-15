
import os
import glob
import codecs
import urllib2

from django.http import HttpResponse

import ws_django.ws_globals as ws_globals

def readResource(resName):
    fp = codecs.open(ws_globals.root + '/spc/gettest/' + resName, 'r', 'utf8')
    data = fp.read()
    fp.close()

    return data

def index(request, param):
  html = readResource('index.html') 
  return HttpResponse(html)

