
globalSpeedFudge = 0.00001;

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

var Planet = function(x, y, mass){
    this.x = x;
    this.y = y;
    this.dx = 0;
    this.dy = 0;
    if(0){
        this.dx = (0.05/globalSpeedFudge)*(50 - Math.random()*100);
        this.dy = (0.05/globalSpeedFudge)*(50 - Math.random()*100);
    }
    this.mass = mass;
    this.color = getRandomColor();
    this.colorEdge = getRandomColor();
    this.trail = [];
};

Planet.prototype.draw = function(){
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

    ctx.globalAlpha = 1.0;
};

createWorldObjects = function(world){
    for(var i = 0; i < 100; ++i){
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

movement = function(world){
    for(var i =0; i < world.objects.length; ++i){
        var o = world.objects[i];

        var pos = new Object();
        pos.x = o.x;
        pos.y = o.y;
        o.trail.push(pos);

        if(o.trail.length > 50){
            o.trail.shift();
        }

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

