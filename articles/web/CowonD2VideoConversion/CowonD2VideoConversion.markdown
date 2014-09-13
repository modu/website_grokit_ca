
# Convert Videos for Cowon D2 Using FFmpeg

I own a Cowon D2 and I love it. Unfortunately, it cannot play native videos without being converted for compatibility. The tool that they provide with the mp3 player works well, but is cumbersome and does not work on all platforms.

## How to Get FFmpeg

Ffmpeg should already be installed on recent linux distributions.

For windows, you can [go to their website](http://www.ffmpeg.org/download.html) and compile from source. Unfortunately they don't have a binary ready for a windows install. However, recent distributions of imagemagick ([which can be downloaded here](http://www.imagemagick.org/script/binary-releases.php?ImageMagick=4qlln45eb5t6lmv7uellkvqc82#windows)) come with the ffmpeg binaries. 

## The Command

Just use:

    ffmpeg -i input_video.avi -vcodec libxvid -acodec libmp3lame -s 320x240 output_video.avi

... and then transfer the output video to your Cowon!

## The Factory of Cowon Videos

You can also use the following python script in order to compress _all_ the .avi files in a directory to a format that the cowon will be able to read. It justs applies the above command to every .avi file in the current directory.

    import os

    def aviFilesFFmpegToCowon():
      OUTDIR = 'out'
      EXTOK = '.avi'
      cmd = "ffmpeg -i IN_FILE -vcodec libxvid -acodec libmp3lame -s 320x240 OUT_FILE"
      
      if not os.path.isdir(OUTDIR):
        os.mkdir(OUTDIR)

      file_vdos = []
      for file in os.listdir('.'):
        if file[-4:] == EXTOK:
          file_vdos.append(file)
       
      for file_vdo in file_vdos:
        print( 'File to process: ' + file_vdo )
        
      for file_vdo in file_vdos:
        cmd_custom = cmd.replace('IN_FILE', '"' + file_vdo + '"')
        cmd_custom = cmd_custom.replace('OUT_FILE', '"' + OUTDIR + '/' + file_vdo + '.cowond2"' + EXTOK)
        print( 'Command: ' + cmd_custom )
        os.system(cmd_custom)

Have fun!