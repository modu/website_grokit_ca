
from google.appengine.ext import db

from django import forms

class WebLog(db.Model):
  name = db.StringProperty(required=True)
  msg = db.StringProperty(required=True, multiline=True)
  date_local = db.StringProperty(required=True, multiline=False)
  date = db.DateTimeProperty(auto_now_add=True, required=True)

def webLogToHtml(webLog):
  html = "<p>(%s at %s): %s</p>" % (webLog.name, webLog.date_local, webLog.msg)
  return html
  
def getAllMessages():
  query = WebLog.all()
  query.order('-date')
  return query

def webLogToTuple(request):
  (name, msg) = (request.POST['name_of_sender'], request.POST['message'])
  return (name, msg)

def saveIncomingWebLog(request):
  name = request.POST['name']
  msg = request.POST['msg']
  date_local = request.POST['date']
  
  # Commit the POST data
  e = WebLog(name = name, msg = msg, date_local = date_local)
  e.put()
  
def cleanSlate():
  db.delete(ChatMessage.all())
