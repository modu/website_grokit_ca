
from google.appengine.ext import db

from django import forms

import time
import json

class FractalStore(db.Model):

    # https://developers.google.com/appengine/docs/python/datastore/typesandpropertyclasses
    date = db.FloatProperty(required=False)
    name = db.StringProperty(required=False, multiline=False)
    data = db.StringProperty(required=False)

def get(key):
    #import pdb; pdb.set_trace()

    q = FractalStore.all()
    #q.filter('name=', key)

    fractalCode = None
    for dbe in q.run():
        # @@b1 PERF!        >>
        if dbe.name == key:
            jsond = dbe.data
            fractalCode = json.loads(jsond)["fractal64"]
            break

    return fractalCode

def save(name, jsonD):

    q = FractalStore.all()
    q.filter("name ==", name)

    person = []
    for p in q.run():
        db.delete(p)

    # Add
    jsonD['time'] = time.time()
    ljson = json.dumps(jsonD)
    e = FractalStore(name = name, date = jsonD['time'], data = ljson)
    e.put()

def cleanSlate():

    query = FractalStore.all()
    it = query.run()

    for u in it:
        db.delete(u)

