
import models

from django.http import HttpResponse

CURR_SESSION_TOKEN = 'aj28skhwy26dj'

def get_all_messages(request):
  
  html = '<html><body>__CONTENT__</body></html>'
  html_a = ''
  for msg in models.getAllMessages():
    html_a = html_a + models.webLogToHtml(msg)
  
  html = html.replace('__CONTENT__', html_a)
  
  return HttpResponse(html)
  
def process_incoming_data(request):
  #(name, msg) = (request.POST['name_of_sender'], request.POST['message'])
  if request.POST.get('date') is None or \
     request.POST.get('msg') is None or \
     request.POST.get('name') is None or \
     request.POST.get('type') != 'log':
    return HttpResponse("Error: POST content invalid: %s" % str(request))
  
  #if request.POST.get('session_token') != CURR_SESSION_TOKEN:
  #  return HttpResponse("Error: invalid session token")
  
  models.saveIncomingWebLog(request)
  
  # All went well, ACK
  return HttpResponse("ACK and a good day to you sir")

