"""
@@b1 Come-up with some rule for what to do and not to do in this file.
"""

import ws_django.ws_globals as ws_globals
import webdoc_entry
import manage_webentries

from django.template import Template, Context

def renderListEntries_CleanAndSimple(lstWebdocEntries, title = 'List of All Content'):
  
  fp = open(ws_globals.blogFolder + '/list_webdoc_entries_clean.html')
  t = Template(fp.read())
  fp.close()
  
  html = t.render(Context({'title': title, 'webdoc_entries': lstWebdocEntries}))
  
  return html  

def renderEntry(strEntryName):
  
  fp = open(ws_globals.blogFolder + '/webdoc_entry.html', 'r')
  t = Template(fp.read())
  fp.close()

  fp = open(ws_globals.blogFolder + '/disqus_code.html')
  comments_zone = fp.read()
  fp.close()
  
  cWebdocEntry = webdoc_entry.WebdocEntry()
  #Assumes the title is the same as the data folder
  cWebdocEntry.loadFromDataFolder(strEntryName)

  lstWebdocEntries = manage_webentries.getWebEntries()
  html = t.render(Context({
                           'webdoc_entry': cWebdocEntry, \
                           'webdoc_entries': lstWebdocEntries, \
                           'comments': comments_zone, \
                           'ad_html_code': _getHtmlAdCode()
                           }))
  
  return html

def _getHtmlAdCode():
  
  fp = open(ws_globals.blogFolder + '/google_ad_code.html', 'r')
  html = fp.read()
  fp.close()
  
  #html = "<!-- No ads for now, lucky!! :). -->"
  
  return html

"""
def renderTagList():
  
  dictTagWeb = manage_webentries.getWebEntriesAsDictOfTags()
  
  fp = open(ws_globals.blogFolder + '/tags_list.html')
  t = Template(fp.read())
  fp.close()
  
  html = t.render(Context({'dict_tags_webentries': dictTagWeb}))
  
  return html
"""