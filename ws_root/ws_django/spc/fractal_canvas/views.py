
import os
import glob
import codecs
import json
import hashlib
import base64

from django.http import HttpResponse
import models

jsCode = """
(function(i, j, pixel) {
    if (i * 100 * i * j * j * j * i * 1000 % 100 > 50) {
        pixel.r = Math.sin(i * 2 * 3.141592);
        pixel.g = Math.sin(j * 2 * 3.141592);
        pixel.b = 0;
    } else {
        pixel.r = 0;
        pixel.g = 0;
        pixel.b = 0;
    }
})
"""

def genHash(data):

    h = hashlib.new("sha256")
    h.update(data)
    return h.hexdigest()

def store_fractal(request):

    if request.method == "POST":
        #import pdb; pdb.set_trace()

        jsonin = json.loads(request.body) 
        key = genHash(jsonin["fractal64"])
        models.save(key, jsonin)

        return HttpResponse(json.dumps({'fractalKey': key}))

    return HttpResponse("404")

def index(request, param = ""):
    fh = open('./ws_django/spc/fractal_canvas/index.html', 'r')
    html = fh.read()
    fh.close()

    if param == "":
        html = html.replace('__jscode__', jsCode)
        return HttpResponse(html)
    else:
        b64JS = models.get(param)
        js = base64.b64decode(b64JS)
        html = html.replace('__jscode__', js)
        return HttpResponse(html)

    return HttpResponse("toto")

