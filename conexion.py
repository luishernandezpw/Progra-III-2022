import mysql.connector

class conexion:
    def __init__(self):
        self.connection = mysql.connector.connect(user='root', 
            password='usbw', host='localhost', database='db_academica')
        if self.connection.is_connected():
            print("Conexion establecida con exito")
        else:
            print("Error al establcer la conexion")
            
    def consultar(self, sql):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            return str(e)

    def ejecutar_consultas(self, sql, val):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, val)
            self.connection.commit()
            return "ok"
        except Exception as e:
            return str(e)