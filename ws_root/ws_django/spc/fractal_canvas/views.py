
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

i = i*3.5 - 2.5;
j = j*2 -1;

mIt = 15;
it = 0;
for (x=0,y=0; it < mIt; ++it){
    xt = x*x - y*y + i;
    y = 2*x*y + j;
    x = xt;

    if(x*x+y*y > 4)
        break;
}

pixel.r = it/mIt;
pixel.g = 0.5*it/mIt;
pixel.b = 0.25*it/mIt;

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

