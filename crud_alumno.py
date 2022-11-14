import conexion

db = conexion.conexion()

class crud_alumno:
    def consultar_alumnos(self):
        return db.consultar("select * from alumnos")
        
    def administrar_alumnos(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql="INSERT INTO alumnos (codigo, nombre, direccion, telefono) VALUES(%s,%s,%s,%s)"
                val=(contenido["codigo"], contenido["nombre"], contenido["direccion"], contenido["telefono"])
            elif contenido["accion"]=="modificar":
                sql="UPDATE alumnos SET codigo=%s, nombre=%s, direccion=%s, telefono=%s WHERE idAlumno=%s"
                val=(contenido["codigo"], contenido["nombre"], contenido["direccion"], contenido["telefono"], contenido["idAlumno"])
            elif contenido["eliminar"]:
                sql="DELETE alumnos FROM alumnos WHERE idAlumno=%s"
                val=(contenido["idAlumno"],)
            return db.ejecutar_consultas(sql, val)
        except Exception as e:
            return str(e)
