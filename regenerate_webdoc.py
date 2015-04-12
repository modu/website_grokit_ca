#!/usr/bin/python3.4

import os
import imp
import shutil

if __name__ == '__main__':
  os.chdir('./ws_root/ws_django/webdoc')
  f, filename, desc = imp.find_module('gen_web_from_data', ['.'])
  gen_web_from_data = imp.load_module('gen_web_from_data', f, filename, desc)
  gen_web_from_data.compile_all()
