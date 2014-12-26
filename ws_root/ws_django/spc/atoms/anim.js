
window.requestAnimFrame =
    window.requestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.oRequestAnimationFrame ||
    window.msRequestAnimationFrame ||
    function (callback) {
        window.setTimeout(callback, 1000 / 60);
};

// Global variables accessible everywhere.
var canvas, world;

var World = function () {
    this.objects = []
};

World.prototype.update = function () {
    updateLogic(world);
};

World.prototype.draw = function () {
    drawLogic(world);
};

function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    world.update();
    world.draw();
    requestAnimFrame(update);
}

function start() {
    world = new World();
    createWorldObjects(world);
    update();
}

window.onload = function () {
    canvas = document.getElementById('canvas_main');
    ctx = canvas.getContext('2d');
    canvas.width = 640;
    canvas.height = 480;
    start();
};

