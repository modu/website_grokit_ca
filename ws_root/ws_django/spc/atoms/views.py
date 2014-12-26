
import os
import glob
import codecs
import json
import hashlib
import base64

from django.http import HttpResponse

js_outer = '<script type="text/javascript">%s</script>'
rootDir = './ws_django/spc/atoms'

def index(request, param = ""):
    fh = open(os.path.join(rootDir, 'index.html'), 'r')
    html = fh.read()
    fh.close()

    jsCt = [js_outer % open(os.path.join(rootDir, f), 'r').read() for f in os.listdir(rootDir) if f[-3:] == '.js']
    html = html.replace('__js__', "\n".join(jsCt))

    return HttpResponse(html)

#index(None)

