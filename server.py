from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import crud_alumno

port= 3000
crud_alumno = crud_alumno.crud_alumno()
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)

        if self.path=="/alumno":
            resp = crud_alumno.consultar_alumnos()
            self.send_response(200)
            self.end_headers()
            self.wfile.write( json.dumps(resp).encode('utf-8'))

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        data = self.rfile.read(longitud)
        data = data.decode()
        data = parse.unquote(data)
        data = json.loads(data)
        if self.path=="/alumno":
            resp = crud_alumno.administrar_alumnos(data)
    
        self.send_response(200)
        self.end_headers()
        self.wfile.write(resp.encode('utf-8'))
        
print("Server iniciado en el puerto ", port)
server = HTTPServer(("localhost", port), servidorBasico)
server.serve_forever()