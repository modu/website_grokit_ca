
from google.appengine.ext import db
from django import forms

class WebDocComment(db.Model):
  name_of_commenter = db.StringProperty(required=True)
  message = db.StringProperty(required=True, multiline=True)
  page_commented = db.StringProperty(required=True)
  date = db.DateTimeProperty(auto_now_add=True, required=True)
  
  def __str__(self):
    txt = "name: %s, message: %s, page_commented: %s, date: %s<br>" % \
      (self.name_of_commenter, self.message, self.page_commented, self.date)
    txt = txt.encode('utf-8')
    return txt

# Setup the form to be filled
class CommentOnWebDoc(forms.Form):
  name = forms.CharField()
  message = forms.CharField(widget=forms.Textarea)

def requestCommentToTuple(request):
  (name, msg) = (request.POST['name'], request.POST['message'])
  return (name, msg)

def saveIncomingComment(request, section):
  # Commit the POST data
  (name, msg) = requestCommentToTuple(request)
  page = section
  e = WebDocComment(name_of_commenter = name, message = msg, page_commented = page)
  e.put()

def getAllComments():
  query = WebDocComment.all()
  query.order('-date')
  return query

def getCommentsForPage(strPageName):
  query = WebDocComment.all()
  query.filter('page_commented =', strPageName)
  query.order('-date')
  return query

def cleanSlate():
  db.delete(WebDocComment.all())

