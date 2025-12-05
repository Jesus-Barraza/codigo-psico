from model import sesion
import hashlib
import tkinter as tk
from tkinter import messagebox
import flet as ft
from flet import AlertDialog

class Usuarios():
    @staticmethod
    def codigo(contrasena):
        contra=hashlib.sha512(contrasena.encode()).hexdigest()
        return contra

    @staticmethod
    def closed(event, ventana, dialog):
        dialog.open = False
        ventana.update()

    @staticmethod
    def respuestaSql(respuesta, ventana):
        if respuesta:
            dlg = ft.AlertDialog(
                title=ft.Text("Acción SQL"),
                content=ft.Text("La acción se ha realizado con éxito"),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: Usuarios.closed(e, ventana, dlg))
                ],
                on_dismiss=lambda e: Usuarios.closed(e, ventana, dlg)
            )
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Acción SQL"),
                content=ft.Text("Ha ocurrido un error al realizar la acción, inténtelo más tarde"),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: Usuarios.closed(e, ventana, dlg))
                ],
                on_dismiss=lambda e: Usuarios.closed(e, ventana, dlg)
            )

        ventana.dialog = dlg
        ventana.overlay.append(dlg)
        ventana.update()
        dlg.open = True
        ventana.update()

    @staticmethod
    def inicioSesion(correo, contra, ventana):
        contra=Usuarios.codigo(contra)
        user=sesion.Sesion.iniciarSesion(correo, contra)
        if user:
            Usuarios.respuestaSql(True, ventana)
            return user
        else:
            Usuarios.respuestaSql(False, ventana)
            return None

    @staticmethod
    def registrar(nombre, correo, telefono, contra, ventana):
        contra=Usuarios.codigo(contra)
        regi=sesion.Sesion.registrar(nombre, correo, telefono, contra)
        if regi:
            Usuarios.respuestaSql(regi, ventana)
            return regi
        else:
            Usuarios.respuestaSql(regi, ventana)
            return None

    @staticmethod
    def borrarCuenta(ide):
        cuidado=messagebox.askyesno(title="Borrar cuenta", message="¿Está seguro de borrar su cuenta? Esta acción no se puede deshacer", icon="warning")
        if cuidado:
            borrar=sesion.Sesion.borrarCuenta(ide)
            if borrar:
                noti=messagebox.showinfo(title="Borrar cuenta", message="Se ha borrado la cuenta con éxito")
                return True
            else:
                noti=messagebox.showerror(title="Borrar cuenta", message="No se ha podido borrar la cuenta, inténtelo más tarde")
            return False
        else:
            noti=messagebox.showinfo(title="Borrar cuenta", message="Eliminación cancelada con éxito")
            return False

class Citas():
    @staticmethod
    def obtener_citas_dia(psicologo_id):
        citas=sesion.Citas.obtener_citas_dia(psicologo_id)
        return citas

    @staticmethod
    def obtener_citas_h(psicologo_id):
        citas=sesion.Citas.obtener_citas_h(psicologo_id)
        return citas

    @staticmethod
    def buscarCitas(psicologo_id, var):
        citas=sesion.Citas.buscarCitas(psicologo_id, var)
        return citas

class Estudiantes():
    @staticmethod
    def buscarEstudiantes(var):
        citas=sesion.Students.buscarEstudiante(var)
        return citas

class Tutor():
    @staticmethod
    def buscarTutores(var):
        citas=sesion.Tutores.buscarTutores(var)
        return citas