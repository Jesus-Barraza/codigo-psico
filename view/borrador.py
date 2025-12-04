import tkinter as tk
from tkinter import PhotoImage
from tkcalendar import Calendar
from controller import funciones
import os
from . import menus
import flet as ft
import multiprocessing
from datetime import datetime

class Volver():
    def __init__(self, ventana):
        menus.Menu(ventana)

def iniciarFlet():
    ft.app(target=Volver, assets_dir="img", view=ft.AppView.FLET_APP)

class Menu():
    def __init__(self, ventana, sesion):
        self.color1 = "#5E95D4"
        self.color2 = "#D9D9D9"
        self.color3 = "#000000"
        self.color4 = "#ffffff"
        self.color5 = "#B7B22F"
        self.tema_oscuro=False
        self.hoy=datetime.now()
        ventana.geometry("1920x1080")
        ventana.title("Programa de psicopedagogía")   
        ventana.config(bg="#E2E2E2")  
        self.menuPrincipal(ventana, sesion)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def cambiarTema(self, ventana, sesion, oscuro_var):
        self.tema_oscuro = oscuro_var.get()  # <-- Actualiza valor persistente
        self.modoOscuro(ventana, sesion, self.tema_oscuro)
    
    def modoOscuro(self, ventana, sesion, status):
        # Cambiar colores globales
        if not status:
            # Tema claro
            self.color1 = "#5E95D4"
            self.color2 = "#D9D9D9"
            self.color3 = "#000000"
            self.color4 = "#ffffff"
            self.color5 = "#B7B22F"
            ventana.config(bg="#E2E2E2")
        else:
            # Tema oscuro
            self.color1 = "#353e70"
            self.color2 = "#4b4b4b"
            self.color3 = "#d6d6d6"
            self.color4 = "#323232"
            self.color5 = "#836819"
            ventana.config(bg="#353535")

        # ---- ACTUALIZAR LA PANTALLA ----
        # Limpia todo
        self.borrarPantalla(ventana)

        # Según el número de pantalla, recargar vista
        self.menuConfiguraciones(ventana, sesion)


    def grupoTitulo(self, ventana, sesion, texto, config, num):
        if num!=0:
            self.num=num
        # Frame superior
        frame_superior = tk.Frame(ventana, bg=self.color1, height=200, highlightbackground=self.color5, highlightthickness=3)
        frame_superior.pack(fill="x", side="top")

        # Frame contenedor horizontal
        frame_horizontal = tk.Frame(frame_superior, bg=self.color1)
        frame_horizontal.pack(fill="x", padx=10, pady=10)

        frame_horizontal.columnconfigure(0, weight=1)  # espacio a la izquierda
        frame_horizontal.columnconfigure(1, weight=0)  # título centrado
        frame_horizontal.columnconfigure(2, weight=1)

        # Frame del título (izquierda)
        if num==4 or num==5:
            frame_titulo = tk.Frame(frame_horizontal, bg=self.color3, height=30, width=600)
        else:
            frame_titulo = tk.Frame(frame_horizontal, bg=self.color2, height=30, width=400)
        frame_titulo.grid(row=0, column=1, padx=10)

        lbl_titulo = tk.Label(frame_titulo, text=texto, font=("Arial", 24), fg=self.color3, bg=self.color2)
        lbl_titulo.pack(anchor="center")

        if config:
            # Frame de botones (derecha)
            frame_botones = tk.Frame(frame_horizontal, bg=self.color1)
            frame_botones.grid(row=0, column=2, sticky="e")

            path = os.path.abspath("img/")
            self.button_image_1 = PhotoImage(file=path + "/config.png")
            button_1 = tk.Button(
                frame_botones,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:self.menuConfiguraciones(ventana, sesion),
                relief="flat",
                bg=self.color1
            )
            button_1.pack(side="left", padx=10)

            self.button_image_2 = PhotoImage(file=path + "/noti.png")
            button_2 = tk.Button(
                frame_botones,
                image=self.button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.menuNotificaciones(ventana, sesion),
                relief="flat",
                bg=self.color1
            )
            button_2.pack(side="left", padx=10)
        else:
            #Frame de retorno
            path = os.path.abspath("img/")
            self.button_image_1 = PhotoImage(file=path + "/Atras.png")
            button_1 = tk.Button(
                frame_horizontal,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:retorno(self.num),
                relief="flat",
                bg=self.color1
            )
            button_1.grid(row=0, column=0, padx=10)

            def retorno(num):
                if num==1:
                    button_1.config(command=lambda:self.menuPrincipal(ventana, sesion))
                elif num==2:
                    button_1.config(command=lambda:self.menuCalendario(ventana, sesion))


    def submenu(self,ventana, sesion):
        #funcion
        def cerrarSesion(ventana):
            ventana.destroy()
            p = multiprocessing.Process(target=iniciarFlet)
            p.start()

        #Barra del menú
        menubar=tk.Menu(ventana, bg=self.color1, fg=self.color4)
        ventana.config(menu=menubar)

        #Archivo del menú
        menuarch=tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Menú desplegable", menu=menuarch)
        menuarch.add_command(label="Menú principal", command=lambda:self.menuPrincipal(ventana, sesion))
        menuarch.add_command(label="Calendario", command=lambda:self.menuCalendario(ventana, sesion))
        menuarch.add_command(label="Citas", command=lambda:None)
        menuarch.add_separator()
        menuarch.add_command(label="Alumnos", command=lambda:None)
        menuarch.add_command(label="Tutores", command=lambda:None)
        menuarch.add_separator()
        menuarch.add_command(label="Cerrar sesión", command=lambda:cerrarSesion(ventana))
        menuarch.add_command(label="Acerca de", command=lambda:None)

    def menuPrincipal(self, ventana, sesion):
        #Limpiar la pantalla (por si acaso)
        self.borrarPantalla(ventana)

        #barra superior
        self.submenu(ventana, sesion)

        #Grupo de arriba
        self.grupoTitulo(ventana, sesion, "Menú principal", True, 1)

        #Cuadro de citas del día
        lbl_citas_dia = tk.Label(ventana, text="Citas activas", font=("Arial", 18), fg=self.color3, bg=self.color2)
        lbl_citas_dia.pack(pady=10)

        frame_citas_dia = tk.Frame(ventana, bg=self.color4, height=200, width=600, relief="raised", bd=2)
        frame_citas_dia.pack(pady=20)

        citas_dia=funciones.Citas.obtener_citas_dia(sesion[0])   
        if len(citas_dia) > 0:
            lbl_titulo_citas_0=tk.Label(frame_citas_dia, text="Cita ID", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_0.grid(row=0, column=0, pady=10, padx=5)

            lbl_titulo_citas_1=tk.Label(frame_citas_dia, text="Nombre del alumno", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_1.grid(row=0, column=1, pady=10, padx=5)

            lbl_titulo_citas_2=tk.Label(frame_citas_dia, text="Fecha", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_2.grid(row=0, column=2, pady=10, padx=5)

            lbl_titulo_citas_3=tk.Label(frame_citas_dia, text="Status", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_3.grid(row=0, column=3, pady=10, padx=5)
            num_citas=1

            for cita in citas_dia:
                lbl_cita_0 = tk.Label(frame_citas_dia, text=f"{cita[0]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_0.grid(row=num_citas, column=0, pady=5)

                lbl_cita_1 = tk.Label(frame_citas_dia, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_1.grid(row=num_citas, column=1, pady=5)

                lbl_cita_2 = tk.Label(frame_citas_dia, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_2.grid(row=num_citas, column=2, pady=5)

                lbl_cita_3 = tk.Label(frame_citas_dia, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_3.grid(row=num_citas, column=3, pady=5)

                num_citas += 1
        else:
            lbl_no_citas=tk.Label(frame_citas_dia, text="Por lo pronto, no se han realizado citas", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_no_citas.pack(pady=10)

            btn_interaccion=tk.Button(
                frame_citas_dia,
                text="Agregar cita",
                font=("Arial", 14, "underline"),
                fg="blue",
                bg=self.color4,
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
                command=lambda:None
            )
            btn_interaccion.pack(pady=10)

        #Cuadro de citas pasadas
        lbl_citas_h = tk.Label(ventana, text="Citas activas", font=("Arial", 18), fg=self.color3, bg=self.color2)
        lbl_citas_h.pack(pady=10)

        frame_citas_h = tk.Frame(ventana, bg=self.color4, height=200, width=600, relief="raised", bd=2)
        frame_citas_h.pack(pady=20)

        citas_dia=funciones.Citas.obtener_citas_h(sesion[0])   
        if len(citas_dia) > 0:
            lbl_titulo_citas_0=tk.Label(frame_citas_h, text="Cita ID", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_0.grid(row=0, column=0, pady=10, padx=5)

            lbl_titulo_citas_1=tk.Label(frame_citas_h, text="Nombre del alumno", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_1.grid(row=0, column=1, pady=10, padx=5)

            lbl_titulo_citas_2=tk.Label(frame_citas_h, text="Fecha", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_2.grid(row=0, column=2, pady=10, padx=5)

            lbl_titulo_citas_3=tk.Label(frame_citas_h, text="Status", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_titulo_citas_3.grid(row=0, column=3, pady=10, padx=5)
            num_citas=1

            for cita in citas_dia:
                lbl_cita_0 = tk.Label(frame_citas_h, text=f"{cita[0]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_0.grid(row=num_citas, column=0, pady=5)

                lbl_cita_1 = tk.Label(frame_citas_h, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_1.grid(row=num_citas, column=1, pady=5)

                lbl_cita_2 = tk.Label(frame_citas_h, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_2.grid(row=num_citas, column=2, pady=5)

                lbl_cita_3 = tk.Label(frame_citas_h, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_3.grid(row=num_citas, column=3, pady=5)

                num_citas += 1
        else:
            lbl_no_citas=tk.Label(frame_citas_h, text="No han habido citas recientes", font=("Arial", 16), fg=self.color3, bg=self.color4)
            lbl_no_citas.pack(pady=10)

    def menuCalendario(self, ventana, sesion):
        #borrar pantalla
        self.borrarPantalla(ventana)

        #variable
        fecha=tk.StringVar()

        #Parte superior
        self.submenu(ventana, sesion)        
        self.grupoTitulo(ventana, sesion, "Calendario", True, 2)

        #texto
        cal = Calendar(ventana, selectmode="day", year=self.hoy.year, month=self.hoy.month, day=self.hoy.day, bg=self.color2, fg=self.color3, datepattern="yyyy-mm-dd")
        cal.pack(pady=20)

    def menuNotificaciones(self, ventana, sesion):
        #borrar pantalla
        self.borrarPantalla(ventana)

        #Parte superior
        self.submenu(ventana, sesion)        
        num=self.grupoTitulo(ventana, sesion, "Notificaciones", False, 0)

        #texto
        lbl_status=tk.Label(ventana, text="No hay notificaciones por lo pronto", font=("Arial", 18), fg=self.color3, bg=self.color2)
        lbl_status.pack(pady=20, anchor="center")

    def menuConfiguraciones(self, ventana, sesion):
        #borrar pantalla
        self.borrarPantalla(ventana)

        #variables
        oscuro=tk.BooleanVar(value=self.tema_oscuro)

        #Parte superior
        self.submenu(ventana, sesion)        
        num=self.grupoTitulo(ventana, sesion, "Configuraciones", False, 0)

        #texto
        frame_opciones=tk.Frame(ventana, bg=self.color2)
        frame_opciones.pack(pady=20)

        lbl_status=tk.Label(ventana, text="Activar el modo oscuro", font=("Arial", 18), fg=self.color3, bg=self.color2)
        lbl_status.pack(pady=20, anchor="center")
        switch_modo=tk.Checkbutton(
            frame_opciones,
            text="Modo oscuro",
            font=("Arial", 14),
            fg=self.color3,
            bg=self.color2,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            variable=oscuro,
            command=lambda:self.cambiarTema(ventana, sesion, oscuro)
        )
        switch_modo.pack()

        