from model.conexionBD import *
import hashlib

class Sesion():
    @staticmethod
    def registrar(nombre,email,phone,password):
        try:
            cursor.execute(
                "insert into psychologists values(null,%s,%s,%s,%s)",
                (nombre,email,phone,password,)
            )
            conexion.commit()
            usuario=Sesion.iniciar_sesion(email, password)
            if usuario:
               return True
            else:
               return False
        except:
            return False

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            cursor.execute(
                "select ID_psy, name_psy, mail_psy, phone_psy from psychologists where mail_psy=%s and pass=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
            return None         