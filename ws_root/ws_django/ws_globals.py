"""
@brief Link to global resources

Might seem a bit convoluted, but is build to obtain the same result running on Google App Engine and in local mode (in order to allow direct testing of .py files).
"""

import os.path

thisFileFolder = os.path.split(__file__)[0]

staticFolder = '../static'

blogFolder = 'webdoc'
blogDataFolder = blogFolder + '/data'
blogGeneratedFolder  = blogFolder + '/gen'

thesisFolder = 'masters_thesis'

addSrcFolders = '../../articles/web'
addCPPFolders = '../../articles/web_cs_review'

root                =  os.path.abspath(thisFileFolder)
thesisFolder        =  os.path.abspath(thisFileFolder + '/' + thesisFolder)
blogFolder          =  os.path.abspath(thisFileFolder + '/' + blogFolder)
blogDataFolder      =  os.path.abspath(thisFileFolder + '/' + blogDataFolder)
staticFolder        =  os.path.abspath(thisFileFolder + '/' + staticFolder)
blogGeneratedFolder =  os.path.abspath(thisFileFolder + '/' + blogGeneratedFolder)
addSrcFolders       =  os.path.abspath(thisFileFolder + '/' + addSrcFolders)
addCPPFolders       =  os.path.abspath(thisFileFolder + '/' + addCPPFolders)
