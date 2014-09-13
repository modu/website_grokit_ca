

from django.http import HttpResponse

testhtml = """<!doctype html>
<html>
<head>
  <title>Test App!</title>
</head>
<body>

<canvas id="e" width="800" height="600">
</canvas> 
<script>
var canvas = document.getElementById("e"); 
var context = canvas.getContext("2d"); 
var cat = new Image(); 
cat.src = "../static/TimeForTea_sshot_v1-2.png";
 
cat.onload = function() 
{ 
for (var x = 0, y = 0; x < 500 && y < 375; x += 50, y += 37) 
  { 
    context.drawImage(cat, x, y, 88, 56); 
  } 
};

</script>

</body>
</html>



"""

def index(request):
  return HttpResponse(testhtml)
  


