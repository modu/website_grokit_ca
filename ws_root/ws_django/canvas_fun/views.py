

from django.http import HttpResponse

def index(request):
  fh = open('./ws_django/canvas_fun/my_rad_first_game.html', 'r')
  html = fh.read()
  fh.close()
  return HttpResponse(html)

