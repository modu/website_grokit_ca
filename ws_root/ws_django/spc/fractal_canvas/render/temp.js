
var page = require('webpage').create();
page.open('http://0.0.0.0:8080/spc/fractals/?render=True&b64jsfn=CihmdW5jdGlvbihpLCBqLCBwaXhlbCkgewoKaSA9IGkqMy41IC0gMi41OwpqID0gaioyIC0xOwoKbUl0ID0gMTU7Cml0ID0gMDsKZm9yICh4PTAseT0wOyBpdCA8IG1JdDsgKytpdCl7CiAgICB4dCA9IHgqeCAtIHkqeSArIGk7CiAgICB5ID0gMip4KnkgKyBqOwogICAgeCA9IHh0OwoKICAgIGlmKHgqeCt5KnkgPiA0KQogICAgICAgIGJyZWFrOwp9CgpwaXhlbC5yID0gMC40MCppdC9tSXQ7CnBpeGVsLmcgPSAwLjk1Kml0L21JdDsKcGl4ZWwuYiA9IDAuMjUqaXQvbUl0OwoKfSkK', function() {
    page.viewportSize = {
    width: 512,
    height: 512
    };
    page.render('out_0000.png');
        phantom.exit();
});
