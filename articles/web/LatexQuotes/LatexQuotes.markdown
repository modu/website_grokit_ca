
# Fixing Latex Quotes With a Script

Latex is **great**, but there are a *lot* of small quirks to take account for. Fortunately, since Latex is like code that is compiled, it is quite easy to fix some of the problem with text-processing scripts.

One of my pet peeve is that in order to get nice English quotes to work, Latex requires the user to use non-standard quotes. This is not correct: 'quotes', *this* is correct: `quotes'. Quite annoying when you use a non-English keyboard layout.

I saw that there was no quick solution (e.g. a script that fixes the problem) on [stackoverflow](http://stackoverflow.com/questions/346567/how-can-one-turn-regular-quotes-i-e-into-latex-tex-quotes-i-e).

What the script does is quite simple, it will replace the 'quotes' in your latex document into 'proper latex quotes'. Here is an example of the input-output:

### Input

    This is intended to be a moderately 'hard' test for the 'fixLatexQuotes script'.
    If all goes 'well', it's going to work, without making the file 'kaput'.
    The scrip should 'work in most situations', however, it will not 'try to fix 'compicated' cases'.

### Command Line

    python3 fixLatexQuotes.py fixLatexQuotes_test.tex fixLatexQuotes_test_out.tex

### Output (fixLatexQuotes_test_out.tex)

    This is intended to be a moderately `hard' test for the `fixLatexQuotes script'.
    If all goes `well', it's going to work, without making the file `kaput'.
    The scrip should `work in most situations', however, it will not `try to fix 'compicated' cases'.

### Note

It should fix the quotes properly, but does not try to fix everything (you can see one instance in the example (the indented quote) that is not fixed). The reason is that I guess when it is too hard to make a decision, it should leave the source alone. For my reports it fixes 95% of problems. :)

### The Code!

    #python3 script, put in 'fixLatexQuotes.py'.    
    
    import sys
    import os
    import re

    def do(filename_in, filename_out):
      
      fh = open(filename_in, 'r')
      fc = fh.read()
      fh.close()

      dst = ''
      for line in fc.splitlines():
        line_c = re.sub(r" '([ \w-]+)'", " `\\1'", line)
        if line != line_c:
          print("|{}| -> |{}|".format(line, line_c))
        dst = dst + line_c + '\n'
      
      if filename_out != '':
        fh = open(filename_out, 'w')
        fh.write(dst)
        fh.close()
      else:
        print('No output file specified, changes discarded.')

    if __name__ == '__main__':
      filename_in = sys.argv[1]
      if len(sys.argv) > 2:
        filename_out = sys.argv[2]
      else:
        filename_out = ''
      
      do(filename_in, filename_out)    

### How it Works

It is all in the regex:
    line_c = re.sub(r" '([ \w-]+)'", " `\\1'", line)

The script only applies it on every line. Feel free to tune it and send the improvements!




  

