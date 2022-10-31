from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
port= 3000
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        data = self.rfile.read(longitud)
        data = data.decode()
        data = float(parse.unquote(data))
    
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(data[0][0]).encode())
        
print("Server iniciado en el puerto ", port)
server = HTTPServer(("localhost", port), servidorBasico)
server.serve_forever()