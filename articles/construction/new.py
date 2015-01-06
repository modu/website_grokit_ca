#!/usr/bin/python3

import os
import sys
import argparse
import time

template_meta = """
tags: viewB
date: __time__
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

    os.mkdir(args.name)

    writeTo(args.name, args.name + '.markdown',
            template_md.replace('__title__', args.name))
    writeTo(args.name, args.name + '.meta', template_meta.replace('__time__',
                                                                  time.strftime("%Y-%m-%d", time.localtime())))
    writeTo(args.name, 'compile.py', template_compile)
