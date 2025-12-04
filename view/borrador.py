from tkinter import Tk
from tkinter import messagebox

class Menu():
    def __init__(self, ventana, sesion):
        ventana.geometry("1920x1080")
        ventana.resizable(False, False)
        ventana.title("Programa de psicopedagogía")     
        self.menuPrincipal(ventana, sesion)

    def menuPrincipal(self, ventana, sesion):
        pass

