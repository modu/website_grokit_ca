

from django.http import HttpResponse

def index(request, param):
  return HttpResponse("Not found: %s" % param)

