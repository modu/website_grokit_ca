
# Weight Watch: Monitor Your Weight Efficiently

## News: 2011-01-03: New Version (1.3)

The old version used either (the excellent) matplotlib. Unfortunately, it does not work with python 3. So I ported the graphics generation to [google chart API](http://code.google.com/apis/chart/). The drawback is that you need an internet connexion in order to generate the graphics and that I am now dependent on google. The good news is that the program is much smaller now.

### Google Charts API

Small sample on how to use the 'Google Charts API' to directly generate a .png image without using a browser.

    # build the query with template parameters
    query ="http://chart.apis.google.com/chart?chxl=0:__X_LABELS__&chxp=__X_LABELS_POS__&chxr=0,__MIN_TIME__,__MAX_TIME__|1,__MIN_WEIGHT__,__MAX_WEIGHT__&chxs=0,676767,11.5,0,lt,676767|1,676767,11.5,0,lt,676767&chxt=x,y&chs=800x300&cht=lc&chco=3072F3&chds=__MIN_WEIGHT__,__MAX_WEIGHT__&chd=t:__COMMASEP_WEIGHT__&chdl=Weight&chdlp=b&chls=2,4,1&chma=5,5,5,25&chtt=Your+Weight+Timeline"
    
    [...]
    
    # relace template with data
    query = query.replace('__X_LABELS__', strXLabels)
    query = query.replace('__X_LABELS_POS__', strXLabelsPos)
    query = query.replace('__MIN_TIME__', str(min(lst_dateEpoch)))
    query = query.replace('__MAX_TIME__', str(max(lst_dateEpoch)))
    
    [...]
    
    # use 'urllib.request' to download the data & write to file
    sock = urllib.request.urlopen(query)
    image_bytes = sock.read()
    sock.close()

    fh = open('Weight_GoogleGraphApi.png', 'wb')
    fh.write(image_bytes)
    fh.close()    

## Installation

Just unzip the source in a folder and then

    python3 pyWeight.py
    or
    python3 pyWeight.py --redraw

You will get the following:
    
    How much do you weight now?
    165
    ./Weight.xml written successfully.

You weight history is saved in a .xml file, mirrored in a .csv file and 'plotted' in a .png file.

This is what the program generates for me:

![](../../static/WeightWatch_1p3_sshot_2011-03-04.png)

The screenshot is my actual weight that I have been keeping track with this program since 2007-09-03.

## Download

[pyWeightWatch v1.3 (google charts API)](../../static/weight_watch_v1-3_gcAPI.zip) 

[pyWeightWatch v1.2 (octave)](../../static/weight_watch_v1-2_octave.zip) 

