
var Planet = function(x, y){
    this.x = x;
    this.y = y;
    this.mass = 100;
};

Planet.prototype.draw = function(){
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.mass*0.1, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'green';
    ctx.fill();
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#003300';
    ctx.stroke();
};

createWorldObjects = function(world){
    world.objects.push(new Planet(100, 100));
    world.objects.push(new Planet(150, 150));
};

var dist = function(o1, o2){
    return Math.sqrt( (o1.x - o2.x)*(o1.x - o2.x) + (o1.y - o2.y)*(o1.y - o2.y) );
};

updateLogic = function(world){
    
    for(var i =0; i < world.objects.length; ++i){
        for(var j =0; j < world.objects.length; ++j){

            if(i != j){
                var o1 = world.objects[j];
                var o2 = world.objects[i];
                var d = dist(o1, o2);

                if(d != 0){
                    var attr = 1 / d; 
                    o1.x = o1.x + attr*100;
                }
            }
        }
    }

};

drawLogic = function(world){

    for(var i =0; i < world.objects.length; ++i){
        world.objects[i].draw();
    };

    ctx.beginPath();
    ctx.moveTo(100, 100);
    ctx.lineTo(200, 200);
    ctx.stroke();
};

