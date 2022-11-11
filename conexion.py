import mysql.connector

class conexion:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='usbw',
            database='db_academica'
        )
        if self.db.is_connected():
            print("Conexion establecida con exito")
        else:
            print("Error en la conexion")
    def consultar(self, sql):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()

    def ejecutar_consulta(self, sql, val):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, val)
            self.db.commit()
            return "ok"
        except Exception as e:
            return str(e)