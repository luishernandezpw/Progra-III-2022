from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
port= 3000

#importar las librerias
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

#leer datos de entrenamiento
temperaturas = pd.read_csv("datos.csv", sep=";")
print(temperaturas["celsius"])

#datos de entrada y salida
celsius = temperaturas["celsius"]
fahrenheit = temperaturas["fahrenheit"]

#modelo de entrenamiento
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compilar elmodelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

#entrenar el modelo
epocas = modelo.fit(celsius, fahrenheit, epochs=150, verbose=1)

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
        f = modelo.predict([data])
    
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(f[0][0]).encode())
        
print("Server iniciado en el puerto ", port)
server = HTTPServer(("localhost", port), servidorBasico)
server.serve_forever()