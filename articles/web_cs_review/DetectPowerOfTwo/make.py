#!/usr/bin/python3

import os

files = os.listdir('.')

filesc = [file for file in files if file[-3:].lower() == 'cpp']

rv = 0
for file in filesc:
    cmd = 'g++ -std=c++11 %s -o %s.bin' % (file, file)
    #cmd = 'clang -std=c++11 %s -o %s.bin' % (file, file)
    print(cmd)
    rv |= os.system(cmd)

if rv == 0:
    os.system('./' + filesc[0] + '.bin')
