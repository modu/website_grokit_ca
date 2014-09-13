
from google.appengine.api import mail

def notifyNewComment(strCommentContent):
  
  #Disable sending e-mail
  if 0:
    message = mail.EmailMessage(sender="<disabled@gmail.com>",
                                subject="New comment on site")

    message.to = "Admin <disabled@gmail.com>"
    message.body = """
    __CONTENT__
    """
    message.body = message.body.replace('__CONTENT__', strCommentContent)
    
    # Make sure everything is a-OK
    message.check_initialized()
    # Send it!
    message.send()
  


