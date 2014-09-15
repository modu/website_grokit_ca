
import webdoc_entry
import webdoc_render
import models
import notify_new_comment

import manage_webentries
import ws_django.ws_globals as ws_globals

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Template, Context
import django

def index(request, param = ''):
     
  if param == '':
    html = renderMainPage()      
  else:
    if param == 'all':
        # Magic param!
        html = renderListAll()
    else:
        html = webdoc_render.renderEntry(param)

  return HttpResponse(html)

def readResource(resName):
    fp = open(ws_globals.blogFolder + '/' + resName, 'r')
    data = fp.read()
    fp.close()

    return data
  
def renderMainPage():

    # Only display "important" entries.
    webEntries = manage_webentries.getWebEntriesMatchingTag('viewA')
    
    html_webEntriesList = webdoc_render.renderListEntries_CleanAndSimple(webEntries, title = '')

    t = Template(readResource('tags_cloud.html'))
    dictTagImp = manage_webentries.getDictTagImportance()
    tag_cloud_html = t.render(Context({'dict_tags_importance': dictTagImp}))  
    
    t = Template(readResource('main_page.html'))
    
    html = t.render(Context({'main_list': html_webEntriesList, 'tags_cloud': tag_cloud_html}))
    
    return html

def renderListAll():
    
    webEntries = manage_webentries.getWebEntries()
    html = webdoc_render.renderListEntries_CleanAndSimple(webEntries, title = '')
    
    t = Template(readResource('list_all.html'))
    
    html = t.render(Context({'list_all': html}))
    
    return html

def tags(request, param = ''):
  
  requested_tag = param
  
  lstWebdocEntries = manage_webentries.getWebEntries()
  
  lstWebdocEntriesWithRightTag = []
  for webdocEntry in lstWebdocEntries:
    if requested_tag in webdocEntry.getTags():
        lstWebdocEntriesWithRightTag.append(webdocEntry)
  
  if len(lstWebdocEntriesWithRightTag) > 0:
    html = webdoc_render.renderListEntries_CleanAndSimple(lstWebdocEntriesWithRightTag, title = 'List of Content with Tag: %s' % requested_tag)
  else:
    html = '<h3>no article with tag: %s</h3>' % requested_tag
    
  return HttpResponse(html)
  
"""  
def incoming_comment(request, section):
  
  models.saveIncomingComment(request, section)
  
  #Send e-mail
  (name, msg) = models.requestCommentToTuple(request)
  notify_new_comment.notifyNewComment(name + ' : ' + msg)
  
  return HttpResponseRedirect('..#prevcomments')
"""