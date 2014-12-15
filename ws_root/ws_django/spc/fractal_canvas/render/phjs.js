var page = require('webpage').create();
page.open('http://0.0.0.0:8080/spc/fractals/?render=True', function() {
    page.viewportSize = {
          width: 512,
          height: 512
    };
    page.render('out.png');
    phantom.exit();
});
