
import os
os.chdir('./movie')

#cmd = "ffmpeg -framerate 1 -pattern_type glob -i '*.png' -c:v libx264 out.mp4"
#cmd = "ffmpeg -f image2 -i out_%05d.png -q:v 1 ../a.mpg"
cmd = "convert -delay 3 -quality 100 *.png ../movie.gif"

print(cmd)

os.system(cmd)

