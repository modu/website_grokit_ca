
js = """
var page = require('webpage').create();
page.open('http://0.0.0.0:8080/spc/fractals/__html_param__', function() {
    page.viewportSize = {
    width: 512,
    height: 512
    };
    page.render('__file_out__');
        phantom.exit();
});
"""
