from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

#importar las librerias necesarias
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

port = 3000

temperaturas = pd.read_csv('datos.csv', sep=";")
#print(temperaturas)

#datos de entrenamiento
c = temperaturas["celsius"]
f = temperaturas["fahrenheit"]

#modelo de entrenamiento, con 1 capa densa (Oculta)
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compilar el modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), 
    loss="mean_squared_error")

#entrenar el modelo
epocas = modelo.fit(c,f, epochs=200, verbose=0)

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        lenc = int(self.headers["Content-Length"])
        data = self.rfile.read(lenc)
        data = data.decode()
        data = float(parse.unquote(data))

        #probar nuestra IA
        resp = modelo.predict([data])

        self.send_response(200)
        self.end_headers()
        self.wfile.write( str(resp[0][0]).encode() )

print("Servidor corriendo en el pueto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()