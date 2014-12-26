
globalSpeedFudge = 0.0001;

var Planet = function(x, y, mass){
    this.x = x;
    this.y = y;
    this.dx = 0;
    this.dy = 0;
    this.mass = mass;
    this.color = '#009700';
};

Planet.prototype.draw = function(){
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.mass*0.1, 0, 2 * Math.PI, false);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#1033ff'; 
    ctx.stroke();
};

createWorldObjects = function(world){
    if(0){
        world.objects.push(new Planet(100, 100, 100));
        world.objects.push(new Planet(150, 150, 50));
        world.objects.push(new Planet(350, 150, 250));
    }

    for(var i = 0; i < 200; ++i){
        var planet = new Planet(world.dx * Math.random(), world.dy * Math.random(), 400 * Math.random() * Math.random());
        world.objects.push(planet);
    }
};

var dist = function(o1, o2){
    return Math.sqrt( (o1.x - o2.x)*(o1.x - o2.x) + (o1.y - o2.y)*(o1.y - o2.y) );
};

var direction = function(o1, o2){
    var v = new Object();
    v.x = o2.x-o1.x;
    v.y = o2.y-o1.y;

    magn = Math.sqrt( v.x*v.x + v.y*v.y );
    v.x = v.x/magn;
    v.y = v.y/magn;
    return v;
};

gravity = function(world){
    // Bug: this will act twice per object -- only act once per pair?
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

movement= function(world){
    for(var i =0; i < world.objects.length; ++i){
        var o = world.objects[i];
        o.x += o.dx * globalSpeedFudge;
        o.y += o.dy * globalSpeedFudge;
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

