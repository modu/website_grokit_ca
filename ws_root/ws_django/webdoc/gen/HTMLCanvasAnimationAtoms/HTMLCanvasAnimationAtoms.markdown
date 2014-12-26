
# anim.js to Create Simple Interactive Canvas Elements

This is a simple demo on how to do animations using HTML5 canvas. You can just steal the bare-bone anim.sj which will take care to animate everything as long as you provide the following three JavaScript functions:

    createWorldObjects(world)
    drawLogic(world)
    updateLogic(world)

If you look in atom.js ([you can check all the most up to dates file on git-hub here](https://github.com/grokit/website_grokit_ca/blob/master/articles/web/HTMLCanvasAnimationAtoms)), you see that this is pretty simple:

    createWorldObjects = function(world){
      for(var i = 0; i < 100; ++i){
        var planet = new Planet(world.dx * Math.random(), world.dy * Math.random(), 400 * Math.random() * Math.random());
        world.objects.push(planet);
      }
    };

    updateLogic = function(world){
      gravity(world);
      movement(world);
    };

    drawLogic = function(world){
      for(var i =0; i < world.objects.length; ++i){
        world.objects[i].draw();
      };
    };

The only thing to remember is to make sure all the objects that you add to the world have a draw() function.

# atom.js How Does It Work

You can inspect the code, but the gist of it is just the gravity function which pulls the object proportional to distance and mass:

    gravity = function(world){
      for(var i =0; i < world.objects.length; ++i){
        for(var j =0; j < world.objects.length; ++j){

          if(i != j){
            var o1 = world.objects[j];
            var o2 = world.objects[i];
            var d = dist(o1, o2);

            if(d > 1){
              var v = direction(o1, o2);
              var attr = o2.mass / d*d;
              o1.dx += v.x*attr;
              o1.dy += v.y*attr;
            }
          }
        }
      }
    };

The only thing left to do is to draw the circles proportional to their mass.

# How Can I Have Fun Modifying This?

You can just save this page as an .html file, edit it and run it in your browser. The JavaScript is embedded in the HTML so you do not need a server to play with it, just modify it and run in your browser.

# A Little Bit of Algorithms

In order to run the simulation, you have to calculate the
