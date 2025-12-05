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
            usuario=Sesion.iniciarSesion(email, password)
            if usuario:
               return True
            else:
               return False
        except:
            return False

    @staticmethod
    def iniciarSesion(email, contrasena):
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
    
    def borrarCuenta(ide):
        try:
            cursor.execute(
                "delete from psychologists where ID_psy=%s",
                (ide,)
            )
            conexion.commit()
            return True
        except:
            return False
        
class Citas():
    @staticmethod
    def obtener_citas_dia(psicologo_id):
        try:
            cursor.execute(
                "select ID_app, students.name_stu, date, status from appointments JOIN students ON FK_stu=students.control_num where FK_psy=%s and date >= CURDATE() order by date",
                (psicologo_id,)
            )
            citas=cursor.fetchall()
            return citas
        except:
            return []
        
    @staticmethod
    def obtener_citas_h(psicologo_id):
        try:
            cursor.execute(
                "select ID_app, students.name_stu, date, status from appointments JOIN students ON FK_stu=students.control_num where FK_psy=%s and date < CURDATE() order by date DESC",
                (psicologo_id,)
            )
            citas=cursor.fetchall()
            return citas
        except:
            return []

    @staticmethod
    def buscarCitas(psicologo_id, var):
        try:
            if len(var):
                cursor.execute(
                    "select ID_app, students.name_stu, date, status from appointments join students on FK_stu=students.control_num where FK_psy=%s and students.name_stu like %s order by date DESC",
                    (psicologo_id, f"%{var}%")
                )
                citas=cursor.fetchall()
                return citas
            else:
                cursor.execute(
                    "select ID_app, students.name_stu, date, status from appointments join students on FK_stu=students.control_num where FK_psy=%s order by date DESC",
                    (psicologo_id, )
                )
                citas=cursor.fetchall()
                return citas
        except:
            return []

class Students():
    @staticmethod
    def buscarEstudiante(var):
        try:
            if len(var):
                cursor.execute(
                    "SELECT name_stu, control_num, CONCAT(groups.period, ' ', groups.group_code, ' ', groups.modal, ' ', groups.carrer), mail_stu, phone_stu, cont_app, susp FROM `students` JOIN groups on FK_group=groups.ID_group where name_stu like %s",
                    (f"%{var}%", )
                )
                citas=cursor.fetchall()
                return citas
            else:
                cursor.execute(
                    "SELECT name_stu, control_num, CONCAT(groups.period, ' ', groups.group_code, ' ', groups.modal, ' ', groups.carrer), mail_stu, phone_stu, cont_app, susp FROM `students` JOIN groups on FK_group=groups.ID_group"
                )
                citas=cursor.fetchall()
                return citas
        except:
            return []

class Tutores():
    @staticmethod
    def buscarTutores(var):
        try:
            if len(var):
                cursor.execute(
                    "SELECT name_tea, CONCAT(groups.period, ' ', groups.group_code, ' ', groups.modal, ' ', groups.carrer), mail_tea, phone_tea FROM `tutored` JOIN groups on FK_group=groups.ID_group where name_tea like %s",
                    (f"%{var}%", )
                )
                citas=cursor.fetchall()
                return citas
            else:
                cursor.execute(
                    "SELECT name_tea, CONCAT(groups.period, ' ', groups.group_code, ' ', groups.modal, ' ', groups.carrer), mail_tea, phone_tea FROM `tutored` JOIN groups on FK_group=groups.ID_group"
                )
                citas=cursor.fetchall()
                return citas
        except:
            return []
