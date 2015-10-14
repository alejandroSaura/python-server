import time
import BaseHTTPServer
import json

# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    """Sum two numbers passed by URL."""

    path = s.path    
    path = path[1:]
    parameters = path.split("+")

    result = int(parameters[0]) + int(parameters[1])

    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>Title goes here.</title></head>")
    s.wfile.write("<body><p>This is a sum test: put the sum of two numbers in the URL</p>")
    s.wfile.write("<p>Your operation: %s + %s = %s</p>" % (parameters[0], parameters[1], result))
    
    s.wfile.write("</body></html>")

    responseObject = {'firstNumber': int(parameters[0]), 'secondNumber': int(parameters[1]), 'result': result}
    jsonObject = json.dumps(responseObject)
    




httpd = BaseHTTPServer.HTTPServer(("0.0.0.0", 8000), MyHandler)
httpd.serve_forever()