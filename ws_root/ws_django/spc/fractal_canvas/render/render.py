
import os

url = "http://0.0.0.0:8080/spc/fractals/55c92a32ea85ecb05b79a94018291c6236873d68078a208bd34983c53a9a8a94?render"
cmd = "phantomjs rs.js %s out.png" % url

os.system(cmd)


