from model import sesion
import hashlib
import tkinter as tk
from tkinter import messagebox

class Usuarios():
    @staticmethod
    def codigo(contrasena):
        contra=hashlib.sha512(contrasena.encode()).hexdigest()
        return contra

    @staticmethod
    def inicio_sesion(correo, contra):
        contra=Usuarios.codigo(contra)
        user=sesion.Sesion.iniciar_sesion(correo, contra)
        if user:
            return user
        else:
            return None

    @staticmethod
    def registrar(nombre, apellido, correo, contra):
        contra=Usuarios.codigo(contra)
        regi=sesion.Sesion.registrar(nombre, apellido, correo, contra)
        if regi:
            return regi
        else:
            noti=messagebox.showerror(title="Registro", message="No se ha podido registrar al usuario, inténtelo más tarde")
            return None

class Citas():
    @staticmethod
    def obtener_citas_dia(psicologo_id):
        citas=sesion.Citas.obtener_citas_dia(psicologo_id)
        return citas
    
    def obtener_citas_h(psicologo_id):
        citas=sesion.Citas.obtener_citas_h(psicologo_id)
        return citas