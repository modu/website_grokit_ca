
import ws_django.ws_globals as ws_globals
import ws_django.webdoc as webdoc
import ws_django.webdoc.webdoc_render as webdoc_render
import ws_django.webdoc.manage_webentries as manage_webentries

from django.http import HttpResponse
from django.template import Template, Context

import os
import glob
import codecs

def readResource(resName):
    fp = codecs.open(ws_globals.root + '/spc/computer_science_review/' + resName, 'r', 'utf8')
    data = fp.read()
    fp.close()

    return data

def index(request, param):
    
    tags = manage_webentries.getWebEntriesAsDictOfTags()
    
    #raise Exception(str(tags))
    
    csiq_trees = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_trees'])
    #csiq_linkedlist = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_linkedlist'])
    csiq_hash = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_hash'])
    csiq_elementary = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_elementary'])
    binary_search = webdoc_render.renderListEntries_CleanAndSimple(tags['binary search'])
    csiq_sort = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_sort'])
    csiq_combinatorics = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_combinatorics'])
    #csiq_binary = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_binary'])
    #csiq_string = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_string'])
    csiq_graph = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_graph'])
    #csiq_math = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_math'])
    csiq_heap = webdoc_render.renderListEntries_CleanAndSimple(tags['csiq_heap'])
    
    t = Template(readResource('main.html'))
    html = t.render(Context({'csiq_trees': csiq_trees,
                             #'csiq_linkedlist': csiq_linkedlist,
                             'csiq_hash': csiq_hash,
                             'csiq_elementary': csiq_elementary,
                             'binary_search': binary_search,
                             'csiq_sort': csiq_sort,
                             'csiq_combinatorics': csiq_combinatorics,
                             #'csiq_binary': csiq_binary,
                             #'csiq_string': csiq_string,
                             'csiq_graph': csiq_graph,
                             #'csiq_math': csiq_math,
                             'csiq_heap': csiq_heap,
                             'ads': _getHtmlAdCode()
                             }))
    
    return HttpResponse(html)

def _getHtmlAdCode():
  
  fp = open(ws_globals.blogFolder + '/google_ad_code.html', 'r')
  html = fp.read()
  fp.close()
  
  return html
