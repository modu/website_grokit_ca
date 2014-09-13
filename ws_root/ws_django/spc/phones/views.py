
import os
import glob
import codecs

from django.http import HttpResponse

def index(request, param):
  
  if len(param) < 5 or param[0:2] != '!!':
    return HttpResponse('<html><body>No such phone.</body></html>')
  
  search = param[2:].lower()
  
  fh = codecs.open('./ws_django/spc/phones/phones.dat', 'r', 'utf8')
  plines = fh.readlines()
  fh.close()
  
  match = []
  
  for l in plines:
    if search in l.lower():
        match.append(l)
  
  html = '<html><body><h1>Phones</h1>%s</body></html>' % "<br>".join(match)
  
  return HttpResponse(html)

