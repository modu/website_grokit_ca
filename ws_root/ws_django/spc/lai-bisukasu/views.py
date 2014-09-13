
import os
import glob
import codecs

from django.http import HttpResponse

html_head = """
<html>
<body>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>lai-bisukasu</title>
<script type="text/javascript">
</script>
<style media="screen" type="text/css">

body {
    margin: 20px 0;
    margin-left: 225px;
    margin-right: 225px;
    background: #F5F5F5;
}

body, th, td, input, textarea {
	font-family: Helvetica;
	font-size: 13px;
	color: #080808;
}

h1, h2, h3 {
	margin-top: 0.5em;
	font-family: Helvetica;
	color: #626456;
}

h1 {
	letter-spacing: -.075em;
	font-size: 3em;
}

h2 {
	letter-spacing: -.05em;
	font-size: 1.8em;
	font-weight: normal;
	color: #8D8E85;
}

h3 {
	font-size: 1.3em;
}

#fable_fr {
  margin-left: 10px;
  position: absolute;
  left: 10%;
  top: 150px;
  font-size: 0.9em;
  width: 35%;
}

#fable_en {
  margin-left: 10px;
  position: absolute;
  right: 10%;
  top: 150px;
  font-size: 0.9em;
  width: 35%;
}

</style>
</head>

"""

html_end = """
</body>
</html>
"""    
    
def index(request, param):
  
  #thisdir = './static'
  #files = os.listdir(thisdir)
  
  html = html_head
  html += "<h1>lai-bisukasu</h1>"
  html += '<p><img alt="" src="../../../../static/lai-bisukasu.png" /></br>'
  #html += " ".join(files)
  html += """
<audio controls autoplay>
  <source src="../../../../static/cat10.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>  
  """
  html += html_end
  
  return HttpResponse(html)

