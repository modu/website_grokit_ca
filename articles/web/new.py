#!/usr/bin/python3

import os
import sys
import argparse

template_meta = """
tags: viewA
date: 2014-99-99
category: auto 
"""

template_compile = """
def isCustomCompile():
  return False
"""

template_md = """
# __title__
"""

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    args = parser.parse_args()
    return args

def writeTo(folder, filename, content):
    fh = open(os.path.join(folder, filename), 'w')
    fh.write(content)
    fh.close()

if __name__ == '__main__':
    args = getArgs()
    print(args)

    os.mkdir(args.name)

    writeTo(args.name, args.name + '.markdown', template_md.replace('__title__', args.name))
    writeTo(args.name, args.name + '.meta', template_meta)
    writeTo(args.name, 'compile.py', template_compile)




