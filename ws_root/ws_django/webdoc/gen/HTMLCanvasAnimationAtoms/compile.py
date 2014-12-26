import os
import shutil

def isCustomCompile():
  return True 

def genHtml(folderOut):

    files = os.listdir('.')
    for f in files:
        shutil.copyfile(f, os.path.join(f, os.path.join(folderOut, f)))
    fh = open(os.path.join(folderOut, 'index.html'), 'w')
    fh.write('popo')
    fh.close()
