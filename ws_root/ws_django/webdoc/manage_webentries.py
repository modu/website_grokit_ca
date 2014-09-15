
import ws_django.ws_globals as ws_globals
import webdoc_entry

from django.http import HttpResponse

import os
import os.path
import math

def getWebEntries():
  lstEntries = []
  entriesFolders = os.listdir(ws_globals.blogGeneratedFolder)
  #Remove non-directories
  entriesFolders = [folder for folder in entriesFolders if \
                 os.path.isdir( ws_globals.blogGeneratedFolder + '/' + folder)]
  #Remove folders that contain '__'
  entriesFolders = [folder for folder in entriesFolders if folder.find('__') == -1]
  
  for folder in entriesFolders:
    cWebdocEntry = webdoc_entry.WebdocEntry()
    cWebdocEntry.loadFromDataFolder(folder)
    if cWebdocEntry.isWebReady():
      lstEntries.append(cWebdocEntry)
    #@tag Need a logger! Printed output ends up in html on web!??!
    #else:
    #  print("Skipping '%s' because it has been tagged as 'noweb'." % cWebdocEntry)
  lstEntries.sort()
  return lstEntries

def getWebEntriesMatchingTag(tag):
    lstEntries = getWebEntries()

    webEntriesDisplay = []

    for we in lstEntries:
        if tag in we.getTags():
            webEntriesDisplay.append(we)  
    
    return webEntriesDisplay

def getWebEntriesAsDictOfCategories():
  
  lstEntries = getWebEntries()
  
  #Build a dictionary of category -> webentry
  dictCatWeb = {}
  for entry in lstEntries:
    strCat = entry.getCategory()
    if strCat is None:
      strCat = 'None'
    strCat = strCat.lower()
    
    if not dictCatWeb.has_key( strCat ):
      dictCatWeb[strCat] = []
    
    dictCatWeb[strCat].append( entry )
  
  return dictCatWeb

def getWebEntriesAsDictOfTags():
  
  lstEntries = getWebEntries()
  
  #Build a dictionary of tag -> [webentry]
  dictTags = {}
  for entry in lstEntries:
    lstTags = entry.getTags()
    
    for tag in lstTags:
        if not dictTags.has_key( tag ):
            dictTags[tag] = []
        
        dictTags[tag].append( entry )
  
  return dictTags

def getWebEntriesTagsStrength():
  lstEntries = getWebEntries()
  
  dictTagWeb = {}
  for entry in lstEntries:
    lstTag = entry.getTags()
   
    for strTag in lstTag:
      
      if not dictTagWeb.has_key( strTag ):
        dictTagWeb[strTag] = 0
    
      dictTagWeb[strTag] += 1
  
  return dictTagWeb

def getDictTagImportance():
  dictWETags = getWebEntriesTagsStrength()
  
  # dim the difference between a lot and a few
  for key, value in dictWETags.items():
    dictWETags[key] = pow(value, 0.1)
  #
  # normalize values: max: max_d, min: min_d
  #
  
  max_d = 5
  min_d = 2
  
  max_v = max(dictWETags.values())
  min_c = min(dictWETags.values())
  
  f_b = float(max_d - min_d) / float(max_v - min_c)
  f_a = min_d - (min_c * f_b)
  
  dictWEImp = {}
  for key, value in dictWETags.items():
    val_renorm = value*f_b + f_a
    dictWEImp[key] = int(round(val_renorm))
  
  return dictWEImp
