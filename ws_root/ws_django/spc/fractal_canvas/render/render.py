
import os
import base64
import tempfile

js = """
var page = require('webpage').create();
page.open('__url__', function() {
    page.viewportSize = {
    width: 512,
    height: 512
    };
    page.render('__file_out__');
        phantom.exit();
});
"""

jsfn = """
(function(i, j, pixel) {

i = i*3.5 - 2.5;
j = j*2 -1;

mIt = 15;
it = 0;
for (x=0,y=0; it < mIt; ++it){
    xt = x*x - y*y + i;
    y = 2*x*y + j;
    x = xt;

    if(x*x+y*y > 4)
        break;
}

pixel.r = 0.40*it/mIt;
pixel.g = 0.95*it/mIt;
pixel.b = 0.25*it/mIt;

})
"""

def render(js, jsfn, filename):
    
    jsfn = base64.b64encode(jsfn.encode()).decode()
    url = "http://0.0.0.0:8080/spc/fractals/?render=True&b64jsfn=%s" % jsfn 

    js = js.replace('__url__', url)
    js = js.replace('__file_out__', filename)

    fh = tempfile.NamedTemporaryFile(delete=False)
    fh.write(js.encode())
    fh.close()

    open('temp.js', 'w').write(js)

    cmd = 'phantomjs "%s" out.png' % (fh.name)

    print(cmd)
    os.system(cmd)

render(js, jsfn, "out_0000.png")

