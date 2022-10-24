from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
port= 3000

#importar las librerias
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#leer datos de entrenamiento
temperaturas = pd.read_csv("grados.csv", sep=";")
print(temperaturas["celsius"])


class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        data = self.rfile.read(longitud)
        data = data.decode()
        data = parse.unquote(data)
        

print("Server iniciado en el puerto ", port)
server = HTTPServer(("localhost", port), servidorBasico)
server.serve_forever()