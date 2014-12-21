
import ws_django.ws_globals as ws_globals

import os
import re

class WebdocMetadata:

  def __init__(self):
    "Raw string of the lines in the metadata file"
    self.__metaDict = {}

  def getDate(self):
    #Date is unique and required
    assert( len(self.__metaDict['date']) == 1 )
    return self.__metaDict['date'][0]

  def getTags(self):
    if not self.__metaDict.has_key('tags'):
      return None
    else:
      return self.__metaDict['tags']

  def getCategory(self):
    #Category is unique, not required
    if not self.__metaDict.has_key('category'):
      return None
    else:
      if not( len(self.__metaDict['category']) <= 1 ):
          raise Exception(">1 category for meta: %s." % self.__metaDict)
      return self.__metaDict['category'][0]

  def isTagPresent(self, strTag):
    return self.__metaDict['tags'].count(strTag) > 0

  def loadFile(self, filename):
    #print("loadFile: " + filename)

    fh = open(filename, 'r')
    metaLines = fh.readlines()
    fh.close()

    #.meta file format to python dictionary
    for line in metaLines:
      if line.find(':') == -1:
        continue
      assert( len(line.split(':')) == 2 )
      metaTag = line.split(':')[0]
      self.__metaDict[metaTag] = []
      for metaTagItem in line.split(':')[1].split(','):
        if metaTagItem.strip() != '':
          self.__metaDict[metaTag].append(metaTagItem.strip())

  def toHtml(self):

    htmlMeta = '<h4>Page Metadata</h4><div id="metainfo">'
    for key, val in self.__metaDict.iteritems():
      htmlMeta = htmlMeta + '%s: %s<br>' % (key, val)
    htmlMeta = htmlMeta + '</div>'

    return str(htmlMeta)

class WebdocEntry:

  def __init__(self):
    self.__title = None

  def __cmp__(self, other):
    if self.getDate() > other.getDate():
      return -1
    else:
      return 1

  def getTitle(self):
    return self.__title

  def getBriefDescription(self):
    return self.getTitle()

  def getTags(self):
    return self.__metadata.getTags()

  def getEntrySubUrl(self):
    return self.__entrySubUrl

  def getDate(self):
    return self.__metadata.getDate()

  def getCategory(self):
    return self.__metadata.getCategory()

  def getMetaDescription(self):
    return self.getTitle()

  def getMetaKeywords(self):
    str = ", ".join(self.__metadata.getTags())
    str = self.__metadata.getCategory() + ", " + str
    return str

  def isWebReady(self):
    if self.__metadata.isTagPresent('noweb'):
      return False
    else:
      return True

  def toHtml(self):
    assert self.__html != None
    return self.__html

  def __tryFindTitleFromHtml(self, html):
    title = None

    #Use the first '<h1>' tag found in html
    for html_line in html.splitlines():
      m = re.match(r"<h1>(.*)</h1>", html_line)
      if m is not None and len(m.groups()) is not 0:
        title = m.groups()[0]
        break

    return title

  def loadFromDataFolder(self, dataFolder):

    #Locate html file
    path = ws_globals.blogGeneratedFolder + '/' + dataFolder.lower()
    files = []

    # Correct a path that came lower-cased.
    if not os.path.isdir(path):
      allF = os.listdir(ws_globals.blogGeneratedFolder)
      fMap = {x.lower(): x for x in allF}
      path = ws_globals.blogGeneratedFolder + '/' + fMap[dataFolder.lower()]

    if os.path.isdir(path):
      files = os.listdir(path)
    else:
      raise Exception("Cannot find path: %s (df: %s)." % (path, dataFolder))

    htmlFile = None
    for file in files:
      if file.find('.html') != -1:
        htmlFile = file

    #Copy to html answer
    if htmlFile is not None:
      fh = open(path + '/' + htmlFile, 'r')
      self.__html = fh.read()
      fh.close()

    if self.__html is None:
        raise Exception("Could not find html")

    #Provide a sub-url
    self.__entrySubUrl = dataFolder

    #Try to provide a title from html
    #@tag Should put tags there, as well as provide a special metadata field in order to override
    #@tag this is done at RUNTIME! --> move this to pre-computed data!
    self.__title = dataFolder + ': ' + str(self.__tryFindTitleFromHtml(self.__html))
    #Failback = use source folder as title
    if self.__title is None:
      self.__title = dataFolder

    #Insert footer with metadata
    metaFile = None
    for file in files:
      if file.find('.meta') != -1:
        metaFile = file
    if metaFile is not None:
      webdocMetadata = WebdocMetadata()
      webdocMetadata.loadFile(path + '/' + metaFile)
      self.__metadata = webdocMetadata

      self.__html = self.__html + webdocMetadata.toHtml()
