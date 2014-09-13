
import django
from django.http import HttpResponse

import ws_django.webdoc.models

def index(request):
  html = """
<h1> Debug Page </h1>
"""
  html = html + '<p> Using django v%s </p>' % str(django.VERSION)
  
  return HttpResponse(html)

def dump_dbs(request):
  comments = ws_django.webdoc.models.getAllComments()
  html = '<h1>Comments</h1>'
  for comment in comments:
    html = html + str(comment)
  html = html + '<h1>Done!</h1>'
  return HttpResponse(html)
  
