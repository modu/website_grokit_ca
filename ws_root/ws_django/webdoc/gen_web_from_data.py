"""
@brief Generate the files served by the website from various data sources
@note  Works with python 2.7 and 3.1

TODO
- [] Be able to process a single document w/o recompiling whole ws
"""

import os
import os.path
import shutil
import sys
import imp
import codecs
import re

import markdown

# Backward way to import from parent dir in a script.
#
# See:
#   - http://www.python.org/dev/peps/pep-0366/
#   - http://stackoverflow.com/questions/1096216/override-namespace-in-python/1096247#1096247
f, filename, desc = imp.find_module('ws_globals', ['..'])
ws_globals = imp.load_module('ws_globals', f, filename, desc)

STATIC_FILES_EXT = ['.jpg', '.png', '.zip', '.tar.gz', '.pdf', '.exe', '.svg', '.wav']

def customPreProcessing(fileContent):
    
    toInsert = re.findall("dext.insertCode\('.*?'\)", fileContent, re.MULTILINE)
    
    for i in toInsert:
        
        filename = i.split("('")[1].split("')")[0]
        
        fh = codecs.open(filename, 'r', 'utf-8')
        fc = fh.readlines()
        fh.close()
        
        fcc = []
        fcc.append('**[Inserted file: %s.]**\n\n' % filename)
        for line in fc:
            fcc.append('    %s' % line)
        
        # Very inefficient, but oh well, this is pre-computed.
        fileContent = fileContent.replace(i, "".join(fcc))        
    
    return fileContent
    

def defaultGenHtml(directoryOut):
  
  filesProcess = []    
  for file in os.listdir('.'):
    if file.find('.meta') != -1 and file.find('~') == -1:
      src = os.getcwd() + '/' + file
      dst = directoryOut + '/' + file
      print( "copy {0} to {1}".format(src, dst) )
      shutil.copy(src, dst)
    if file.find('.markdown') != -1 and file.find('~') == -1:
      filesProcess.append(file)
  
  for file in filesProcess:
    file_out = directoryOut + '/' + file + str('.html')
    
    fh = codecs.open(file, 'r', "utf-8")
    file_cnt = fh.read()
    fh.close()
    
    file_cnt = customPreProcessing(file_cnt)
    
    md = markdown.Markdown()
    html = md.convert(file_cnt)
    
    fh = codecs.open(file_out, 'w', "utf-8")
    fh.write(html)
    fh.close()

def compile_folder(path, name):
  
  # Execute the compile directive found in folder
  foundContent = False
  files = []  
  if os.path.isdir(path):
    files = os.listdir(path)
  
  metaF = [f for f in files if os.path.splitext(f)[1] == '.meta']
  print(metaF)
  assert len(metaF) <= 1

  if len(metaF) == 1:
      metaF = metaF[0]
      fh = open(os.path.join(path, metaF), 'r')
      if fh.read().find('no_publish') != -1:
          print('Skipping html compile of %s because found meta no_publish marker.' % metaF)
          return

  for file in files:
    if file == 'compile.py':
      oldPath = os.getcwd()
      os.chdir(path)
      
      sys.path.append(path)
      # Clear cache or else only the first import will matter.
      try:
          del sys.modules[file.strip('.py')]
      except KeyError:
          pass      
      imp_mod = __import__( file.strip('.py') )
      sys.path.remove(path)
      
      path_out = ws_globals.blogGeneratedFolder + '/' + name
      
      if not os.path.isdir(path_out):
        os.makedirs(path_out)
      
      # print('Folder %s isCustom?: %s' % (path, imp_mod.isCustomCompile()))
      
      # @@bug change for return html, then do a sanity check
      if imp_mod.isCustomCompile() == False:
        defaultGenHtml(path_out)
      else:
        assert imp_mod.isCustomCompile() == True
        imp_mod.genHtml(path_out)
      
      foundContent = True
      
      os.chdir(oldPath)
  
  ## Copy the files to the static folder

  # Refresh files (can be created by compile)  
  files = []
  if os.path.isdir(path):
    files += os.listdir(path)
  # Copy
  if foundContent:
    for file in files:
      for ext in STATIC_FILES_EXT:
        if file.find(ext) != -1:
          src = path + '/' + file
          dst = ws_globals.staticFolder + '/' + file
          cmd = "copy %s to %s" % (src, dst)
          print(cmd)
          assert not os.path.isfile(dst) # avoid collisions
          #try:
          shutil.copy(src, dst)
          #except IOError:
          #  print ("error: could not copy {} to {}".format(src, dst))

def compile_all():
  
  # Delete the 'gen' (generated) folder
  if os.path.isdir(ws_globals.blogGeneratedFolder):
    shutil.rmtree(ws_globals.blogGeneratedFolder)
  os.mkdir(ws_globals.blogGeneratedFolder)    
  open(ws_globals.blogGeneratedFolder + '/_hg_dir_tag_', 'w').close() # touch for hg dir-keep

  # Delete all files in static folder (not an accumulator of junk!)
  shutil.rmtree(ws_globals.staticFolder)
  os.mkdir(ws_globals.staticFolder)
  open(ws_globals.staticFolder + '/_hg_dir_tag_', 'w').close() # touch for hg dir-keep
  
  # Copy the global css files
  cssFolder = '../css'
  files = os.listdir(cssFolder)
  for file in files:
    src = cssFolder + '/' + file
    dst = ws_globals.staticFolder + '/' + file
    print("copy %s to %s" % (src, dst))
    shutil.copy(src, dst)
  
  #Copy gfx
  gfxDir = '../gfx'
  for file in os.listdir(gfxDir):
    src = gfxDir + '/' + file
    dst = ws_globals.staticFolder + '/' + file
    print("copy %s to %s" % (src, dst))
    shutil.copy(src, dst)
  
  # Process...
  blogFolders = os.listdir(ws_globals.blogDataFolder)
  newFolders = os.listdir(ws_globals.addSrcFolders)
  cppFolders = os.listdir(ws_globals.addCPPFolders)
  allFolders = []
  for blogFolder in blogFolders:
    allFolders.append( ws_globals.blogDataFolder + '/' + blogFolder )
  for newFolder in newFolders:
    allFolders.append( ws_globals.addSrcFolders + '/' + newFolder )
  for cppFolder in cppFolders:
    allFolders.append( ws_globals.addCPPFolders + '/' + cppFolder )
  
  for folder in allFolders:
    name = folder.split('/')[-1]
    compile_folder(folder, name)

if __name__ == "__main__":
  compile_all()
