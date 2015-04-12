import os
import shutil

import markdown


def isCustomCompile():
    return True

js_outer = '<script type="text/javascript">%s</script>'


def genHtml(folderOut):

    files = os.listdir('.')
    files = [f for f in files if f.find('__pycache') == -1]

    for f in files:
        shutil.copyfile(f, os.path.join(f, os.path.join(folderOut, f)))

    fh = open('index.html', 'r')
    html = fh.read()
    fh.close()

    rootDir = '.'
    jsCt = [js_outer % open(os.path.join(rootDir, f), 'r').read()
            for f in os.listdir(rootDir) if f[-3:] == '.js']
    html = html.replace('__js__', "\n".join(jsCt))

    md = markdown.Markdown()
    mdFile = [f for f in os.listdir('.') if '.markdown' in f][0]
    mDhtml = md.convert(open(mdFile).read())
    html = html.replace('__markdown__', mDhtml)

    fh = open(os.path.join(folderOut, 'index.html'), 'w')
    fh.write(html)
    fh.close()
