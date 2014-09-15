
# Compress Images Using ImageMagick

The quality factor of the .jpg format is largerly unknown. This result in a lot of images that are easily four to five time as big as they need to be (for the same 'visible' quality).

The method that I am going to show here is going to reduce the size of every picture in a directory to about 500k. This compression will reduce the quality of the picture, but not enough to make it noticeable to the naked eye.

First of all, go download the excellent ImageMagick software at http://www.imagemagick.org/ (dl: [win](http://www.imagemagick.org/script/binary-releases.php#windows), [linux](http://www.imagemagick.org/script/binary-releases.php#unix))

Once the software is installed, go to the directory containing the files (it would be wise to back-up your pictures first) and type in the command line:

    mogrify -resize "2048x2048>" -quality 75 *.jpg

What it will do is that it will take each picture individually, resize it to 2048x[...] pixels and change the quality setting. I chose 75 because it yields the greatest compression/quality loss ratio. Check it out for yourself, I am sure you can't tell the difference between the compressed picture and the original. This typically reduces the size of a 3,000 Kb picture to under 500Kb.

Here are some other cool things you can do with ImageMagick intalled:

    Get the picture properties:
      identify -verbose abc.jpg

    Compare the diff between two pictures:
      compare -metric MAE First. png Second.jpg diff.png

    Burn a logo into a pic:
      (more on composing: http://www.imagemagick.org/Usage/compose/)
      (Use white background)
      composite -gravity NorthWest -compose color-burn logo.png image.jpg out.jpg

    Write text on all pictures:
      (x,y , dx,dy) 0,0 = original size
      mogrify -draw "image color-burn 4,4 0,0 'logo.png'" *.jpg
      convert -draw "image color-burn 4,4 0,0 'logo.png'" *.jpg out.jpg

More at:

* http://www.imagemagick.org/script/composite.php
* http://www.imagemagick.org/Usage/

