
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

    gravityInner = function(left, right){
      var d = dist(left, right);

      if(d > 1){
        var v = direction(left, right);
        var attr = right.mass / d*d;
        left.dx += v.x*attr;
        left.dy += v.y*attr;
      }
    };

    gravity = function(world){
      for(var i =0; i < world.objects.length; ++i){
        for(var j = i+1; j < world.objects.length; ++j){
          gravityInner(world.objects[i], world.objects[j]);
          gravityInner(world.objects[j], world.objects[i]);
        }
      }
    };

The only thing left to do is to draw the circles proportional to their mass:

    Planet.prototype.draw = function(){
      ctx.globalAlpha = 1.0;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.mass*0.1, 0, 2 * Math.PI, false);
      ctx.fillStyle = this.color;
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = this.colorEdge;
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(this.x, this.y);
      for(var i = this.trail.length-1; i >= 0; --i){
        var p = this.trail[i];
        ctx.lineTo(p.x, p.y);
      }
      ctx.lineWidth = this.mass/20;
      ctx.lineCap = 'round';
      ctx.globalAlpha = 0.4;
      ctx.stroke();
    };

## A Little Bit of Algorithms

In order to run the simulation, you have to calculate the pull that each planet exercises on each other planet, which costs n^2. Now, it would be possible to disregard the effect of far-way objects ([doing so would reduce the cost to n log(n) -- see Barnes-Hut simulation](http://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation)), but for simplicity's sake we are not doing this here.

Another little trick that is fun to observe is that the inner loop starts at _j=i+1_. A more natural way would by to have a nested loop of the form:

    gravity = function(world){
      for(var i =0; i < world.objects.length; ++i){
        for(var j = 0; j < world.objects.length; ++j){
          if(i!=j){
            gravityInner(world.objects[i], world.objects[j]);
          }
        }
      }
    };

There is probably no significant difference in terms of performance, but looking at why the _j=i+1_ trick works is interesting. Let's say you have four items: a, b, c, d. Using the function above, you generate:

    a, a
    a, b
    a, c
    a, d

    b, a
    b, b
    b, c
    b, d

    c, a
    c, b
    c, c
    c, d

    d, a
    d, b
    d, c
    d, d

... and skip the case where i==j (a,a; b,b; ...). The _j=i+1_ trick will generate the following:

    a, b
    a, c
    a, d

    b, c
    b, d

    c, d

... which is basically outputting all the pairs. Using _j=i+1_ is akin to observing that when you are at letter, all the previous letters have already been paired with the current letter. So if you modify the inner function to generate the symmetric pairs (a,b -> a,b; b,a), you end-up with the same result.

# How Can I Have Fun Modifying This?

You can just save this page as an .html file, edit it and run it in your browser. The JavaScript is embedded in the HTML so you do not need a server to play with it, just modify it and run in your browser.
