from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import alumno
import json
port = 3000

alumno = alumno.alumno()
class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
            
        if(self.path=="/alumno"):
            len = int(self.headers["Content-Length"])
            data = self.rfile.read(len)
            data = data.decode()
            data = parse.unquote(data)
            data = json.loads(data)

            resp = alumno.consultar(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write( json.dumps(resp).encode() )

    def do_POST(self):
        lenc = int(self.headers["Content-Length"])
        data = self.rfile.read(lenc)
        data = data.decode()
        data = parse.unquote(data)
        data = json.loads(data)
        if self.path=="/alumno":
            resp = alumno.aministrar_alumnos(data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write( str(resp).encode() )

print("Servidor corriendo en el pueto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()