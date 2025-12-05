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
        self.color2 = "#E2E2E2"
        self.color3 = "#000000"
        self.color4 = "#ffffff"
        self.color5 = "#B7B22F"
        self.tema_oscuro=False
        self.hoy=datetime.now()
        ventana.geometry("1920x1080")
        ventana.title("Programa de psicopedagogía")   
        ventana.config(bg=self.color2)  
        self.menuPrincipal(ventana, sesion)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def limit_float(p):
        allowed = "0123456789."
        if all(ch in allowed for ch in p) and p.count(".") <= 1:
            return True
        else:
            return False

    @staticmethod
    def limit_int(p):
        if p.isdigit():
            return True
        else:
            return False

    @staticmethod
    def limit_mail(p):
        allowed = "0123456789.abcdefghijklmnopqrstuvwxyz@_"
        if all(ch in allowed for ch in p) and p.count("@") <= 1:
            return True
        else:
            return False

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
            ventana.config(bg=self.color2)
        else:
            # Tema oscuro
            self.color1 = "#353e70"
            self.color2 = "#353535"
            self.color3 = "#d6d6d6"
            self.color4 = "#323232"
            self.color5 = "#836819"
            ventana.config(bg=self.color2)

        # ---- ACTUALIZAR LA PANTALLA ----
        # Limpia todo
        self.borrarPantalla(ventana)

        # Según el número de pantalla, recargar vista
        self.menuConfiguraciones(ventana, sesion)

    def grupoTitulo(self, ventana, sesion, texto, config, num):
        if num!=0 and num!=6:
            self.num=num
        # Frame superior
        if num==6:
            frame_superior = tk.Frame(ventana, bg=self.color5, height=200, highlightbackground=self.color3, highlightthickness=3)
        else:
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
            frame_titulo = tk.Frame(frame_horizontal, bg=self.color5, height=30, width=600)
            lbl_titulo = tk.Label(frame_titulo, text=texto, font=("Arial", 24), fg=self.color3, bg=self.color5)
        else:
            frame_titulo = tk.Frame(frame_horizontal, bg=self.color2, height=30, width=400)
            lbl_titulo = tk.Label(frame_titulo, text=texto, font=("Arial", 24), fg=self.color3, bg=self.color2)
        frame_titulo.grid(row=0, column=1, padx=10)
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
                elif num==3:
                    button_1.config(command=lambda:self.menuCitas(ventana, sesion))
                elif num==4:
                    button_1.config(command=lambda:self.menuEstudiantes(ventana, sesion))
                elif num==5:
                    button_1.config(command=lambda:self.menuTutores(ventana, sesion))

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
        menuarch.add_command(label="Citas", command=lambda:self.menuCitas(ventana, sesion))
        menuarch.add_separator()
        menuarch.add_command(label="Alumnos", command=lambda:self.menuEstudiantes(ventana, sesion))
        menuarch.add_command(label="Tutores", command=lambda:self.menuTutores(ventana, sesion))
        menuarch.add_separator()
        menuarch.add_command(label="Cerrar sesión", command=lambda:cerrarSesion(ventana))
        menuarch.add_command(label="Acerca de", command=lambda:self.acercaDe(ventana, sesion))

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
                lbl_cita_0.grid(row=num_citas, column=0, pady=5, padx=10)

                lbl_cita_1 = tk.Label(frame_citas_dia, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_1.grid(row=num_citas, column=1, pady=5, padx=10)

                lbl_cita_2 = tk.Label(frame_citas_dia, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_2.grid(row=num_citas, column=2, pady=5, padx=10)

                lbl_cita_3 = tk.Label(frame_citas_dia, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_3.grid(row=num_citas, column=3, pady=5, padx=10)

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
        lbl_citas_h = tk.Label(ventana, text="Citas anteriores", font=("Arial", 18), fg=self.color3, bg=self.color2)
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
                lbl_cita_0.grid(row=num_citas, column=0, pady=5, padx=10)

                lbl_cita_1 = tk.Label(frame_citas_h, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_1.grid(row=num_citas, column=1, pady=5, padx=10)

                lbl_cita_2 = tk.Label(frame_citas_h, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_2.grid(row=num_citas, column=2, pady=5, padx=10)

                lbl_cita_3 = tk.Label(frame_citas_h, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                lbl_cita_3.grid(row=num_citas, column=3, pady=5, padx=10)

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

        #calendario
        cal = Calendar(ventana, selectmode="day", year=self.hoy.year, month=self.hoy.month, day=self.hoy.day, bg=self.color2, fg=self.color3, datepattern="yyyy-mm-dd")
        cal.pack(pady=20)

        #texto
        lbl_status=tk.Label(ventana, text="Esta es una función beta y no funciona de normal", font=("Arial", 12), fg=self.color3, bg=self.color2)
        lbl_status.pack(pady=20, anchor="center")

    def menuNotificaciones(self, ventana, sesion):
        #borrar pantalla
        self.borrarPantalla(ventana)

        #Parte superior 
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
        num=self.grupoTitulo(ventana, sesion, "Configuraciones", False, 0)

        #definicion
        def cerrarSesion(ventana, sesion):
            status=funciones.Usuarios.borrarCuenta(sesion[0])
            if status:
                ventana.destroy()
                p = multiprocessing.Process(target=iniciarFlet)
                p.start()

        #texto
        switch_modo=tk.Checkbutton(
            ventana,
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
        switch_modo.pack(pady=20)
        
        #boton
        btn_eliminarcuenta=tk.Button(
            ventana,
                text="Eliminar cuenta",
                font=("Arial", 20, "underline"),
                fg="red",
                bg=self.color2,
                cursor="hand2",
                command=lambda:cerrarSesion(ventana, sesion),
                width=30,
                height=2
            )
        btn_eliminarcuenta.pack(pady=50, side="bottom")

    def menuCitas(self, ventana, sesion):
        self.borrarPantalla(ventana)

        #variables
        buscador=tk.StringVar()
        buscador.set("")

        #Menú de arriba
        self.submenu(ventana, sesion)
        num=self.grupoTitulo(ventana, sesion, "Citas", True, 3)

        #Buscador
        frame_busqueda=tk.Frame(ventana, width=500, height=50, bg=self.color2)
        frame_busqueda.pack(pady=5)

        txt_buscador=tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        self.button_image_3 = PhotoImage(file=path + "/search.png")
        button_3 = tk.Button(
            frame_busqueda,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:buscar(sesion[0], buscador.get()),
            relief="flat",
            bg=self.color4
        )
        button_3.grid(row=0, column=1, padx=2)

        #frame de las citas
        frame_lista=tk.Frame(ventana, bg=self.color4, height=600, width=800)
        frame_lista.pack(pady=20)

        #funciones
        def buscar(ide, research):
            for widget in frame_lista.winfo_children():
                widget.destroy()
            data=funciones.Citas.buscarCitas(ide, research)
            if len(data) > 0:
                lbl_titulo_citas_0=tk.Label(frame_lista, text="Cita ID", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_citas_0.grid(row=0, column=0, pady=10, padx=5)

                lbl_titulo_citas_1=tk.Label(frame_lista, text="Nombre del alumno", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_citas_1.grid(row=0, column=1, pady=10, padx=5)

                lbl_titulo_citas_2=tk.Label(frame_lista, text="Fecha", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_citas_2.grid(row=0, column=2, pady=10, padx=5)

                lbl_titulo_citas_3=tk.Label(frame_lista, text="Status", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_citas_3.grid(row=0, column=3, pady=10, padx=5)
                num_citas=1

                for cita in data:
                    lbl_cita_0 = tk.Label(frame_lista, text=f"{cita[0]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_0.grid(row=num_citas, column=0, pady=5, padx=10)

                    lbl_cita_1 = tk.Label(frame_lista, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_1.grid(row=num_citas, column=1, pady=5, padx=10)

                    lbl_cita_2 = tk.Label(frame_lista, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_2.grid(row=num_citas, column=2, pady=5, padx=10)

                    lbl_cita_3 = tk.Label(frame_lista, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_3.grid(row=num_citas, column=3, pady=5, padx=10)

                    num_citas += 1
            else:
                lbl_no_citas=tk.Label(frame_lista, text="No hay citas registradas en la base de datos", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_no_citas.pack(pady=10)
            
            ventana.update()
        
        buscar(sesion[0], "")

        #Botones
        frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
        frame_botones.pack(pady=20)
        
        btn_anadir=tk.Button(
            frame_botones,
            text="Añadir",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.insertar(ventana, sesion, 1),
        )
        btn_anadir.grid(row=0, column=0, padx=20)

        btn_modificar=tk.Button(
            frame_botones,
            text="Modificar",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.actualizar(ventana, sesion, 1),
        )
        btn_modificar.grid(row=0, column=1, padx=20)

        btn_eliminar=tk.Button(
            frame_botones,
            text="Eliminar",
            font=("Arial", 20, "underline"),
            fg="red",
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.eliminar(ventana, sesion),
        )
        btn_eliminar.grid(row=0, column=2, padx=20)

    def menuEstudiantes(self, ventana, sesion):
        self.borrarPantalla(ventana)

        #variables
        buscador=tk.StringVar()
        buscador.set("")

        #Menú de arriba
        self.submenu(ventana, sesion)
        num=self.grupoTitulo(ventana, sesion, "Estudiantes", True, 4)

        #Buscador
        frame_busqueda=tk.Frame(ventana, width=500, height=50, bg=self.color2)
        frame_busqueda.pack(pady=5)

        txt_buscador=tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        self.button_image_3 = PhotoImage(file=path + "/search.png")
        button_3 = tk.Button(
            frame_busqueda,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:buscar(buscador.get()),
            relief="flat",
            bg=self.color4
        )
        button_3.grid(row=0, column=1, padx=2)

        #frame de los estudiantes
        frame_lista=tk.Frame(ventana, bg=self.color4, height=600, width=800)
        frame_lista.pack(pady=20)

        #funciones
        def buscar(research):
            for widget in frame_lista.winfo_children():
                widget.destroy()
            data=funciones.Estudiantes.buscarEstudiantes(research)
            if len(data) > 0:
                lbl_titulo_stu_0=tk.Label(frame_lista, text="Nombre del alumno", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_0.grid(row=0, column=0, pady=10, padx=5)

                lbl_titulo_stu_1=tk.Label(frame_lista, text="Matrícula", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_1.grid(row=0, column=1, pady=10, padx=5)

                lbl_titulo_stu_2=tk.Label(frame_lista, text="Grupo", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_2.grid(row=0, column=2, pady=10, padx=5)

                lbl_titulo_stu_3=tk.Label(frame_lista, text="Correo", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_3.grid(row=0, column=3, pady=10, padx=5)

                lbl_titulo_stu_4=tk.Label(frame_lista, text="Teléfono", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_4.grid(row=0, column=4, pady=10, padx=5)

                lbl_titulo_stu_5=tk.Label(frame_lista, text="stu individuales", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_5.grid(row=0, column=5, pady=10, padx=5)

                lbl_titulo_stu_6=tk.Label(frame_lista, text="Suspensión", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_stu_6.grid(row=0, column=6, pady=10, padx=5)
                num_stu=1

                for cita in data:
                    lbl_cita_0 = tk.Label(frame_lista, text=f"{cita[0]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_0.grid(row=num_stu, column=0, pady=5, padx=10)

                    lbl_cita_1 = tk.Label(frame_lista, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_1.grid(row=num_stu, column=1, pady=5, padx=10)

                    lbl_cita_2 = tk.Label(frame_lista, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_2.grid(row=num_stu, column=2, pady=5, padx=10)

                    lbl_cita_3 = tk.Label(frame_lista, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_3.grid(row=num_stu, column=3, pady=5, padx=10)

                    lbl_cita_4 = tk.Label(frame_lista, text=f"{cita[4]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_4.grid(row=num_stu, column=4, pady=5, padx=10)

                    lbl_cita_5 = tk.Label(frame_lista, text=f"{cita[5]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_5.grid(row=num_stu, column=5, pady=5, padx=10)

                    lbl_cita_6 = tk.Label(frame_lista, text=f"{cita[6]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_6.grid(row=num_stu, column=6, pady=5, padx=10)
                    num_stu += 1
            else:
                lbl_no_stu=tk.Label(frame_lista, text="No hay alumnos registrados en la base de datos", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_no_stu.pack(pady=10)
            
            ventana.update()
        
        buscar("")

        #Botones
        frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
        frame_botones.pack(pady=20)
        
        btn_anadir=tk.Button(
            frame_botones,
            text="Añadir",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.insertar(ventana, sesion, 2),
        )
        btn_anadir.grid(row=0, column=0, padx=20)

        btn_citar=tk.Button(
            frame_botones,
            text="Citar",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.beta(ventana, sesion),
        )
        btn_citar.grid(row=0, column=1, padx=20)

        btn_consult=tk.Button(
            frame_botones,
            text="Consultar",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.beta(ventana, sesion),
        )
        btn_consult.grid(row=0, column=2, padx=20)

    def menuTutores(self, ventana, sesion):
        self.borrarPantalla(ventana)

        #variables
        buscador=tk.StringVar()
        buscador.set("")

        #Menú de arriba
        self.submenu(ventana, sesion)
        num=self.grupoTitulo(ventana, sesion, "Tutores", True, 5)

        #Buscador
        frame_busqueda=tk.Frame(ventana, width=500, height=50, bg=self.color2)
        frame_busqueda.pack(pady=5)

        txt_buscador=tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        self.button_image_3 = PhotoImage(file=path + "/search.png")
        button_3 = tk.Button(
            frame_busqueda,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:buscar(sesion[0], buscador.get()),
            relief="flat",
            bg=self.color4
        )
        button_3.grid(row=0, column=1, padx=2)

        #frame de los tutores
        frame_lista=tk.Frame(ventana, bg=self.color4, height=600, width=800)
        frame_lista.pack(pady=20)

        #funciones
        def buscar(research):
            for widget in frame_lista.winfo_children():
                widget.destroy()
            data=funciones.Tutor.buscarTutores(research)
            if len(data) > 0:
                lbl_titulo_tutor_0=tk.Label(frame_lista, text="Nombre del tutor", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_tutor_0.grid(row=0, column=0, pady=10, padx=5)

                lbl_titulo_tutor_1=tk.Label(frame_lista, text="Grupo a cargo", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_tutor_1.grid(row=0, column=1, pady=10, padx=5)

                lbl_titulo_tutor_2=tk.Label(frame_lista, text="Correo", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_tutor_2.grid(row=0, column=2, pady=10, padx=5)

                lbl_titulo_tutor_3=tk.Label(frame_lista, text="Teléfono", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_titulo_tutor_3.grid(row=0, column=3, pady=10, padx=5)
                num_tutor=1

                for cita in data:
                    lbl_cita_0 = tk.Label(frame_lista, text=f"{cita[0]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_0.grid(row=num_tutor, column=0, pady=5, padx=10)

                    lbl_cita_1 = tk.Label(frame_lista, text=f"{cita[1]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_1.grid(row=num_tutor, column=1, pady=5, padx=10)

                    lbl_cita_2 = tk.Label(frame_lista, text=f"{cita[2]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_2.grid(row=num_tutor, column=2, pady=5, padx=10)

                    lbl_cita_3 = tk.Label(frame_lista, text=f"{cita[3]}", font=("Arial", 12), fg=self.color3, bg=self.color4)
                    lbl_cita_3.grid(row=num_tutor, column=3, pady=5, padx=10)

                    num_tutor += 1
            else:
                lbl_no_tutor=tk.Label(frame_lista, text="No hay tutores registrados en la base de datos", font=("Arial", 16), fg=self.color3, bg=self.color4)
                lbl_no_tutor.pack(pady=10)
            
            ventana.update()
        
        buscar("")

        #Botones
        frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
        frame_botones.pack(pady=20)
        
        btn_anadir=tk.Button(
            frame_botones,
            text="Añadir",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.insertar(ventana, sesion, 3),
        )
        btn_anadir.grid(row=0, column=0, padx=20)

        btn_consult=tk.Button(
            frame_botones,
            text="Consultar",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.beta(ventana, sesion),
        )
        btn_consult.grid(row=0, column=1, padx=20)

    def acercaDe(self, ventana, sesion):
        self.borrarPantalla(ventana)

        #Parte superior
        num=self.grupoTitulo(ventana, sesion, "Acerca de", False, 6)

        #Texto
        lbl_info=tk.Label(ventana, text="Aquí en el departamento de psicopedagogía nos comprometemos a brindar la atención psicológica necesaria a los estudiantes de este plantel. \n\n -Contacto: \n -Whatsapp: 618 269 99 97 \n -Correo: fernando.vargas@utd.edu.mx", wraplength=600, font=("Arial", 18))
        lbl_info.pack(pady=30)

        path = os.path.abspath("img/")
        self.img_logo = tk.PhotoImage(file=path + "/Logo_utd.png")   # PNG o GIF
        label = tk.Label(ventana, image=self.img_logo)
        label.image = self.img_logo
        label.pack(pady=30)

        lbl_upd=tk.Label(ventana, text="V0.3")
        lbl_upd.pack(pady=15)

    def insertar(self, ventana, sesion, ori):
        self.borrarPantalla(ventana)

        #limitantes
        verificacion_entero=(ventana.register(self.limit_int), "%P")
        verificacion_mail=(ventana.register(self.limit_mail), "%P")

        if ori==1:
            tl=self.grupoTitulo(ventana, sesion, "Insertar citas", False, 0)

            #variables
            estud=tk.StringVar()
            calendar=tk.StringVar()
            
            #funciones
            def estudiante(id_psi, ventana):
                try:
                    dato=SubMenu.subAlumnos(ventana, id_psi)
                    estud.set(dato[0])
                except:
                    pass

            def fecha(ventana):
                try:
                    dato=SubMenu.subCalendario(ventana)
                    calendar.set(dato)
                except:
                    pass

            def insertar(name_stu, date, num_citas):
                entrada, act=funciones.Citas.agregarCita(sesion[0], name_stu, date, num_citas)
                if entrada and act:
                    self.menuCitas(ventana, sesion)

            #Cuadros de texto
            frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
            frame_cuadro.pack(pady=10)

            #Nombre del estudiante
            lbl_estud=tk.Label(frame_cuadro, text="Nombre del estudiante: ", justify="left")
            lbl_estud.grid(row=0, column=0, pady=5)

            txt_estud=tk.Entry(frame_cuadro, textvariable=estud)
            txt_estud.grid(row=1, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_3 = PhotoImage(file=path + "/sumar.png")
            button_3 = tk.Button(
                frame_cuadro,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:estudiante(sesion[0], ventana),
                relief="flat",
                bg=self.color4
            )
            button_3.grid(row=1, column=1, padx=2)

            #Calendario
            lbl_modelo=tk.Label(frame_cuadro, text="Fecha: ", justify="left")
            lbl_modelo.grid(row=2, column=0, pady=5)

            txt_modelo=tk.Entry(frame_cuadro, textvariable=calendar)
            txt_modelo.grid(row=3, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_4 = PhotoImage(file=path + "/sumar.png")
            button_4 = tk.Button(
                frame_cuadro,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:fecha(ventana),
                relief="flat",
                bg=self.color4
            )
            button_4.grid(row=3, column=1, padx=2)

            #Botones
            frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
            frame_botones.pack(pady=20)
            
            btn_anadir=tk.Button(
                frame_botones,
                text="Insertar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:insertar(estud.get(), calendar.get(), 0),
            )
            btn_anadir.grid(row=0, column=0, padx=20)

            btn_modify=tk.Button(
                frame_botones,
                text="Modificar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.actualizar(ventana, sesion, 1),
            )
            btn_modify.grid(row=0, column=1, padx=20)

            btn_salir=tk.Button(
                frame_botones,
                text="Regresar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.menuCitas(ventana, sesion),
            )
            btn_salir.grid(row=0, column=2, padx=20)
        elif ori==2:
            tl=self.grupoTitulo(ventana, sesion, "Insertar estudiantes", False, 0)

            #variables
            nombre=tk.StringVar()
            grupo=tk.StringVar()
            matricula=tk.StringVar()
            correo=tk.StringVar()
            telef=tk.StringVar()
            
            #funciones
            def grupos(ventana, id_psi):
                try:
                    dato=SubMenu.subGrupos(ventana, id_psi)
                    grupo.set(dato[0])
                except:
                    pass

            def insertar(matricula, id_grp, nombre, corr, tel):
                entrada=funciones.Estudiantes.agregarEstudiante(matricula, id_grp, nombre, corr, tel)
                if entrada:
                    self.menuEstudiantes(ventana, sesion)

            #Cuadros de texto
            frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
            frame_cuadro.pack(pady=10)

            #Nombre del estudiante
            lbl_estud=tk.Label(frame_cuadro, text="Nombre del estudiante: ", justify="left")
            lbl_estud.grid(row=0, column=0, pady=5)

            txt_estud=tk.Entry(frame_cuadro, textvariable=nombre)
            txt_estud.grid(row=1, column=0, pady=[0,15])

            #Grupo
            lbl_grupo=tk.Label(frame_cuadro, text="Grupo: ", justify="left")
            lbl_grupo.grid(row=2, column=0, pady=5)

            txt_grupo=tk.Entry(frame_cuadro, textvariable=grupo)
            txt_grupo.grid(row=3, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_3 = PhotoImage(file=path + "/sumar.png")
            button_3 = tk.Button(
                frame_cuadro,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:grupos(ventana, sesion[0]),
                relief="flat",
                bg=self.color4
            )
            button_3.grid(row=3, column=1, padx=2)

            #matricula
            lbl_matri=tk.Label(frame_cuadro, text="Matricula: ", justify="left")
            lbl_matri.grid(row=4, column=0, pady=5)

            txt_matri=tk.Entry(frame_cuadro, textvariable=matricula, validate="key", validatecommand=verificacion_entero)
            txt_matri.grid(row=5, column=0, pady=[0,15])

            #correo
            lbl_correo=tk.Label(frame_cuadro, text="Correo electrónico: ", justify="left")
            lbl_correo.grid(row=6, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=correo, validate="key", validatecommand=verificacion_mail)
            txt_correo.grid(row=7, column=0, pady=[0,15])

            #telefono
            lbl_correo=tk.Label(frame_cuadro, text="Teléfono: ", justify="left")
            lbl_correo.grid(row=8, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=telef, validate="key", validatecommand=verificacion_entero)
            txt_correo.grid(row=9, column=0, pady=[0,15])

            #Botones
            frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
            frame_botones.pack(pady=20)
            
            btn_anadir=tk.Button(
                frame_botones,
                text="Insertar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:insertar(matricula.get(), grupo.get(), nombre.get(), correo.get(), telef.get()),
            )
            btn_anadir.grid(row=0, column=0, padx=20)

            btn_modify=tk.Button(
                frame_botones,
                text="Modificar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.actualizar(ventana, sesion, 2),
            )
            btn_modify.grid(row=0, column=1, padx=20)

            btn_salir=tk.Button(
                frame_botones,
                text="Regresar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.menuEstudiantes(ventana, sesion),
            )
            btn_salir.grid(row=0, column=2, padx=20)
        elif ori==3:
            tl=self.grupoTitulo(ventana, sesion, "Insertar tutores", False, 0)

            #variables
            nombre=tk.StringVar()
            grupo=tk.StringVar()
            correo=tk.StringVar()
            telef=tk.StringVar()
            
            #funciones
            def grupos(ventana, id_psi):
                try:
                    dato=SubMenu.subGrupos(ventana, id_psi)
                    grupo.set(dato[0])
                except:
                    pass

            def insertar(id_grp, nombre, corr, tel):
                entrada=funciones.Tutor.agregarTutor(id_grp, nombre, corr, tel)
                if entrada:
                    self.menuTutores(ventana, sesion)

            #Cuadros de texto
            frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
            frame_cuadro.pack(pady=10)

            #Nombre del estudiante
            lbl_estud=tk.Label(frame_cuadro, text="Nombre del tutor: ", justify="left")
            lbl_estud.grid(row=0, column=0, pady=5)

            txt_estud=tk.Entry(frame_cuadro, textvariable=nombre)
            txt_estud.grid(row=1, column=0, pady=[0,15])

            #Grupo
            lbl_grupo=tk.Label(frame_cuadro, text="Grupo: ", justify="left")
            lbl_grupo.grid(row=2, column=0, pady=5)

            txt_grupo=tk.Entry(frame_cuadro, textvariable=grupo)
            txt_grupo.grid(row=3, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_3 = PhotoImage(file=path + "/sumar.png")
            button_3 = tk.Button(
                frame_cuadro,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:grupos(ventana, sesion[0]),
                relief="flat",
                bg=self.color4
            )
            button_3.grid(row=3, column=1, padx=2)

            #correo
            lbl_correo=tk.Label(frame_cuadro, text="Correo electrónico: ", justify="left")
            lbl_correo.grid(row=4, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=correo, validate="key", validatecommand=verificacion_mail)
            txt_correo.grid(row=5, column=0, pady=[0,15])

            #telefono
            lbl_correo=tk.Label(frame_cuadro, text="Teléfono: ", justify="left")
            lbl_correo.grid(row=6, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=telef, validate="key", validatecommand=verificacion_entero)
            txt_correo.grid(row=7, column=0, pady=[0,15])

            #Botones
            frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
            frame_botones.pack(pady=20)
            
            btn_anadir=tk.Button(
                frame_botones,
                text="Insertar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:insertar(grupo.get(), nombre.get(), correo.get(), telef.get()),
            )
            btn_anadir.grid(row=0, column=0, padx=20)

            btn_modify=tk.Button(
                frame_botones,
                text="Modificar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.actualizar(ventana, sesion, 3),
            )
            btn_modify.grid(row=0, column=1, padx=20)

            btn_salir=tk.Button(
                frame_botones,
                text="Regresar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.menuTutores(ventana, sesion),
            )
            btn_salir.grid(row=0, column=2, padx=20)
        
    def actualizar(self, ventana, sesion, ori):
        self.borrarPantalla(ventana)
        #limitantes
        verificacion_entero=(ventana.register(self.limit_int), "%P")
        verificacion_mail=(ventana.register(self.limit_mail), "%P")

        if ori==1:
            tl=self.grupoTitulo(ventana, sesion, "Actualizar citas", False, 0)

            #variables
            cit=tk.StringVar()
            estud=tk.StringVar()
            calendar=tk.StringVar()
            
            #funciones
            def cita(id_psi, ventana):
                try:
                    datos=SubMenu.subCitas(ventana, id_psi)
                    cit.set(datos[0])
                    estud.set(datos[1])
                    calendar.set(datos[2])
                except:
                    pass

            def estudiante(id_psi, ventana):
                try:
                    dato=SubMenu.subAlumnos(ventana, id_psi)
                    estud.set(dato[0])
                except:
                    pass

            def fecha(ventana):
                try:
                    dato=SubMenu.subCalendario(ventana)
                    calendar.set(dato)
                except:
                    pass

            def actualizar(name_stu, date, id_psicologo, citar):
                entrada=funciones.Citas.modificarCita(name_stu, date, id_psicologo, citar)
                if entrada:
                    self.menuCitas(ventana, sesion)

            #Cuadros de texto
            frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
            frame_cuadro.pack(pady=10)

            #Cita a modificar
            lbl_cit=tk.Label(frame_cuadro, text="Cita a modificar: ", justify="left")
            lbl_cit.grid(row=0, column=0, pady=5)

            txt_cit=tk.Entry(frame_cuadro, textvariable=cit)
            txt_cit.grid(row=1, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_5 = PhotoImage(file=path + "/sumar.png")
            button_5 = tk.Button(
                frame_cuadro,
                image=self.button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:cita(sesion[0], ventana),
                relief="flat",
                bg=self.color4
            )
            button_5.grid(row=1, column=1, padx=2)

            #Nombre del estudiante
            lbl_estud=tk.Label(frame_cuadro, text="Nombre del estudiante: ", justify="left")
            lbl_estud.grid(row=2, column=0, pady=5)

            txt_estud=tk.Entry(frame_cuadro, textvariable=estud)
            txt_estud.grid(row=3, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_3 = PhotoImage(file=path + "/sumar.png")
            button_3 = tk.Button(
                frame_cuadro,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:estudiante(sesion[0], ventana),
                relief="flat",
                bg=self.color4
            )
            button_3.grid(row=3, column=1, padx=2)

            #Calendario
            lbl_modelo=tk.Label(frame_cuadro, text="Fecha: ", justify="left")
            lbl_modelo.grid(row=4, column=0, pady=5)

            txt_modelo=tk.Entry(frame_cuadro, textvariable=calendar)
            txt_modelo.grid(row=5, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_4 = PhotoImage(file=path + "/sumar.png")
            button_4 = tk.Button(
                frame_cuadro,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:fecha(ventana),
                relief="flat",
                bg=self.color4
            )
            button_4.grid(row=5, column=1, padx=2)

            #Botones
            frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
            frame_botones.pack(pady=20)
            
            btn_anadir=tk.Button(
                frame_botones,
                text="Actualizar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:actualizar(estud.get(), calendar.get(), sesion[0], cit.get()),
            )
            btn_anadir.grid(row=0, column=0, padx=20)

            btn_salir=tk.Button(
                frame_botones,
                text="Regresar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.menuCitas(ventana, sesion),
            )
            btn_salir.grid(row=0, column=1, padx=20)
        elif ori==2:
            tl=self.grupoTitulo(ventana, sesion, "Actualizar estudiantes", False, 0)

            #variables
            nombre=tk.StringVar()
            grupo=tk.StringVar()
            matricula=tk.StringVar()
            correo=tk.StringVar()
            telef=tk.StringVar()
            
            #funciones
            def estudiante(id_psi, ventana):
                try:
                    datos=SubMenu.subAlumnos(ventana, id_psi)
                    nombre.set(datos[0])
                    grupo.set(datos[7])
                    matricula.set(datos[1])
                    correo.set(datos[3])
                    telef.set(datos[4])
                except:
                    pass

            def grupos(ventana, id_psi):
                try:
                    dato=SubMenu.subGrupos(ventana, id_psi)
                    grupo.set(dato[0])
                except:
                    pass

            def actualizar(matricula, id_grp, nombre, corr, tel):
                entrada=funciones.Estudiantes.actualizarEstudiante(matricula, id_grp, nombre, corr, tel)
                if entrada:
                    self.menuEstudiantes(ventana, sesion)

            #Cuadros de texto
            frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
            frame_cuadro.pack(pady=10)

            #Nombre del estudiante
            lbl_estud=tk.Label(frame_cuadro, text="Nombre del estudiante: ", justify="left")
            lbl_estud.grid(row=0, column=0, pady=5)

            txt_estud=tk.Entry(frame_cuadro, textvariable=nombre)
            txt_estud.grid(row=1, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_4 = PhotoImage(file=path + "/sumar.png")
            button_4 = tk.Button(
                frame_cuadro,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:estudiante(sesion[0], ventana),
                relief="flat",
                bg=self.color4
            )
            button_4.grid(row=1, column=1, padx=2)

            #Grupo
            lbl_grupo=tk.Label(frame_cuadro, text="Grupo: ", justify="left")
            lbl_grupo.grid(row=2, column=0, pady=5)

            txt_grupo=tk.Entry(frame_cuadro, textvariable=grupo)
            txt_grupo.grid(row=3, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_3 = PhotoImage(file=path + "/sumar.png")
            button_3 = tk.Button(
                frame_cuadro,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:grupos(ventana, sesion[0]),
                relief="flat",
                bg=self.color4
            )
            button_3.grid(row=3, column=1, padx=2)

            #matricula
            lbl_matri=tk.Label(frame_cuadro, text="Matricula: ", justify="left")
            lbl_matri.grid(row=4, column=0, pady=5)

            txt_matri=tk.Entry(frame_cuadro, textvariable=matricula, validate="key", validatecommand=verificacion_entero)
            txt_matri.grid(row=5, column=0, pady=[0,15])

            #correo
            lbl_correo=tk.Label(frame_cuadro, text="Correo electrónico: ", justify="left")
            lbl_correo.grid(row=6, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=correo, validate="key", validatecommand=verificacion_mail)
            txt_correo.grid(row=7, column=0, pady=[0,15])

            #telefono
            lbl_correo=tk.Label(frame_cuadro, text="Teléfono: ", justify="left")
            lbl_correo.grid(row=8, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=telef, validate="key", validatecommand=verificacion_entero)
            txt_correo.grid(row=9, column=0, pady=[0,15])

            #Botones
            frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
            frame_botones.pack(pady=20)
            
            btn_anadir=tk.Button(
                frame_botones,
                text="Actualizar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:actualizar(matricula.get(), grupo.get(), nombre.get(), correo.get(), telef.get()),
            )
            btn_anadir.grid(row=0, column=0, padx=20)

            btn_salir=tk.Button(
                frame_botones,
                text="Regresar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.menuEstudiantes(ventana, sesion),
            )
            btn_salir.grid(row=0, column=1, padx=20)
        elif ori==3:
            tl=self.grupoTitulo(ventana, sesion, "Actualizar tutores", False, 0)

            #variables
            ide=tk.StringVar()
            nombre=tk.StringVar()
            grupo=tk.StringVar()
            correo=tk.StringVar()
            telef=tk.StringVar()
            
            #funciones
            def tutorado(id_psi, ventana):
                try:
                    datos=SubMenu.subTutores(ventana, id_psi)
                    nombre.set(datos[0])
                    grupo.set(datos[4])
                    correo.set(datos[2])
                    telef.set(datos[3])
                except:
                    pass

            def grupos(ventana, id_psi):
                try:
                    dato=SubMenu.subGrupos(ventana, id_psi)
                    grupo.set(dato[0])
                except:
                    pass

            def insertar(id_grp, nombre, corr, tel):
                entrada=funciones.Tutor.actualizarTutor(nombre, id_grp, corr, tel)
                if entrada:
                    self.menuTutores(ventana, sesion)

            #Cuadros de texto
            frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
            frame_cuadro.pack(pady=10)

            #asignar a todos por nombre
            path = os.path.abspath("img/")
            self.button_image_4 = PhotoImage(file=path + "/sumar.png")
            button_4 = tk.Button(
                frame_cuadro,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:tutorado(sesion[0], ventana),
                relief="flat",
                bg=self.color4
            )
            button_4.grid(row=0, column=0, padx=2)

            #Grupo
            lbl_grupo=tk.Label(frame_cuadro, text="Grupo: ", justify="left")
            lbl_grupo.grid(row=1, column=0, pady=5)

            txt_grupo=tk.Entry(frame_cuadro, textvariable=grupo)
            txt_grupo.grid(row=2, column=0, pady=[0,15])

            path = os.path.abspath("img/")
            self.button_image_3 = PhotoImage(file=path + "/sumar.png")
            button_3 = tk.Button(
                frame_cuadro,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:grupos(ventana, sesion[0]),
                relief="flat",
                bg=self.color4
            )
            button_3.grid(row=2, column=1, padx=2)

            #correo
            lbl_correo=tk.Label(frame_cuadro, text="Correo electrónico: ", justify="left")
            lbl_correo.grid(row=3, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=correo, validate="key", validatecommand=verificacion_mail)
            txt_correo.grid(row=4, column=0, pady=[0,15])

            #telefono
            lbl_correo=tk.Label(frame_cuadro, text="Teléfono: ", justify="left")
            lbl_correo.grid(row=5, column=0, pady=5)

            txt_correo=tk.Entry(frame_cuadro, textvariable=telef, validate="key", validatecommand=verificacion_entero)
            txt_correo.grid(row=6, column=0, pady=[0,15])

            #Botones
            frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
            frame_botones.pack(pady=20)
            
            btn_anadir=tk.Button(
                frame_botones,
                text="Actualizar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:insertar(grupo.get(), nombre.get(), correo.get(), telef.get()),
            )
            btn_anadir.grid(row=0, column=0, padx=20)

            btn_salir=tk.Button(
                frame_botones,
                text="Regresar",
                font=("Arial", 20, "underline"),
                fg=self.color3,
                bg=self.color2,
                cursor="hand2",
                command=lambda:self.menuTutores(ventana, sesion),
            )
            btn_salir.grid(row=0, column=1, padx=20)

    def eliminar(self, ventana, sesion):
        self.borrarPantalla(ventana)
        tl=self.grupoTitulo(ventana, sesion, "Eliminar citas", False, 0)

        #variables
        cit=tk.StringVar()
        
        #funciones
        def cita(id_psi, ventana):
            try:
                datos=SubMenu.subCitas(ventana, id_psi)
                cit.set(datos[0])
            except:
                pass

        def eliminar(citar, id_psicologo):
            entrada=funciones.Citas.eliminarCita(citar, id_psicologo)
            if entrada:
                self.menuCitas(ventana, sesion)

        #Cuadros de texto
        frame_cuadro=tk.Frame(ventana, width=1000, height=700, bg=self.color2)
        frame_cuadro.pack(pady=10)

        #Cita a modificar
        lbl_cit=tk.Label(frame_cuadro, text="Cita a modificar: ", justify="left")
        lbl_cit.grid(row=0, column=0, pady=5)

        txt_cit=tk.Entry(frame_cuadro, textvariable=cit)
        txt_cit.grid(row=1, column=0, pady=[0,15])

        path = os.path.abspath("img/")
        self.button_image_5 = PhotoImage(file=path + "/sumar.png")
        button_5 = tk.Button(
            frame_cuadro,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:cita(sesion[0], ventana),
            relief="flat",
            bg=self.color4
        )
        button_5.grid(row=1, column=1, padx=2)

        #Botones
        frame_botones=tk.Frame(ventana, width=1500, height=300, bg=self.color2)
        frame_botones.pack(pady=20)
        
        btn_quitar=tk.Button(
            frame_botones,
            text="Eliminar",
            font=("Arial", 20, "underline"),
            fg="red",
            bg=self.color2,
            cursor="hand2",
            command=lambda:eliminar(cit.get(), sesion[0]),
        )
        btn_quitar.grid(row=0, column=0, padx=20)

        btn_salir=tk.Button(
            frame_botones,
            text="Regresar",
            font=("Arial", 20, "underline"),
            fg=self.color3,
            bg=self.color2,
            cursor="hand2",
            command=lambda:self.menuCitas(ventana, sesion),
        )
        btn_salir.grid(row=0, column=1, padx=20)

    def beta(self, ventana, sesion):
        self.borrarPantalla(ventana)
        self.submenu(ventana, sesion)
        tl=self.grupoTitulo(ventana, sesion, "Aviso del beta", False, 0)
        
        lbl_beta=tk.Label(ventana, text="Esta función no se encuentra disponible por lo pronto")
        lbl_beta.pack(pady=30)


class SubMenu(Menu):
    @staticmethod
    def subCitas(ventana, id_psi):
        submenu = tk.Toplevel(ventana, width=400, height=300, bg="#ffffff")
        submenu.title("Citas")

        buscador = tk.StringVar()

        frame_busqueda = tk.Frame(submenu, bg="#ffffff")
        frame_busqueda.pack(pady=5)

        txt_buscador = tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        button_image_3 = PhotoImage(file=path + "/search.png")
        button_3 = tk.Button(
            frame_busqueda,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:buscar(id_psi, buscador.get()),
            relief="flat",
            bg="#ffffff"
        )
        button_3.image=button_image_3
        button_3.grid(row=0, column=1, padx=2)

        lista = tk.Listbox(submenu, width=80, height=25, selectmode="single")

        def buscar(id_psi, var):
            citas = funciones.Citas.buscarCitas(id_psi, var)
            lista.delete(0, tk.END)
            if citas:
                for cita in citas:
                    opc = f"{cita[0]:<25} | {cita[1]:<50}"
                    lista.insert(tk.END, opc)
            lista.pack(pady=5)
            return citas

        citas= buscar(id_psi, "")

        tk.Button(
            frame_busqueda,
            image=button_image_3,
            command=lambda: buscar(id_psi, buscador.get()),
            bg="#ffffff",
            borderwidth=0
        ).grid(row=0, column=1, padx=2)

        frame_botones = tk.Frame(submenu, bg="#ffffff")
        frame_botones.pack(pady=20)

        def Aceptar():
            try:
                indice = lista.curselection()[0]
                val = citas[indice]
                submenu.resultado = val
            except:
                submenu.resultado = None
            submenu.destroy()

        tk.Button(
            frame_botones,
            text="Seleccionar",
            command=Aceptar
        ).grid(row=0, column=0, padx=20)

        tk.Button(
            frame_botones,
            text="Cancelar",
            command=lambda: submenu.destroy()
        ).grid(row=0, column=1, padx=20)

        # ✅ Esperar a que el submenú se cierre
        submenu.resultado = None
        submenu.wait_window()

        return submenu.resultado

    @staticmethod
    def subAlumnos(ventana, id_psi):
        submenu = tk.Toplevel(ventana, width=400, height=300, bg="#ffffff")
        submenu.title("Alumnos")

        buscador = tk.StringVar()

        frame_busqueda = tk.Frame(submenu, bg="#ffffff")
        frame_busqueda.pack(pady=5)

        txt_buscador = tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        button_image_3 = PhotoImage(file=path + "/search.png")
        button_3 = tk.Button(
            frame_busqueda,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:buscar(buscador.get()),
            relief="flat",
            bg="#ffffff"
        )
        button_3.image=button_image_3
        button_3.grid(row=0, column=1, padx=2)

        lista = tk.Listbox(submenu, width=80, height=25, selectmode="single")

        def buscar(var):
            estud = funciones.Estudiantes.buscarEstudiantes(var)
            lista.delete(0, tk.END)
            if estud:
                for stud in estud:
                    opc = f"{stud[1]:<25} | {stud[0]:<50}"
                    lista.insert(tk.END, opc)
            lista.pack(pady=5)
            return estud

        alumnos= buscar("")

        tk.Button(
            frame_busqueda,
            image=button_image_3,
            command=lambda: buscar(id_psi, buscador.get()),
            bg="#ffffff",
            borderwidth=0
        ).grid(row=0, column=1, padx=2)

        frame_botones = tk.Frame(submenu, bg="#ffffff")
        frame_botones.pack(pady=20)

        def Aceptar():
            try:
                indice = lista.curselection()[0]
                val = alumnos[indice]
                submenu.resultado = val
            except:
                submenu.resultado = None
            submenu.destroy()

        tk.Button(
            frame_botones,
            text="Seleccionar",
            command=Aceptar
        ).grid(row=0, column=0, padx=20)

        tk.Button(
            frame_botones,
            text="Cancelar",
            command=lambda: submenu.destroy()
        ).grid(row=0, column=1, padx=20)

        # ✅ Esperar a que el submenú se cierre
        submenu.resultado = None
        submenu.wait_window()

        return submenu.resultado

    @staticmethod
    def subTutores(ventana, id_psi):
        submenu = tk.Toplevel(ventana, width=400, height=300, bg="#ffffff")
        submenu.title("Tutores")

        buscador = tk.StringVar()

        frame_busqueda = tk.Frame(submenu, bg="#ffffff")
        frame_busqueda.pack(pady=5)

        txt_buscador = tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        button_image_3 = PhotoImage(file=path + "/search.png")
        button_3 = tk.Button(
            frame_busqueda,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:buscar(buscador.get()),
            relief="flat",
            bg="#ffffff"
        )
        button_3.image=button_image_3
        button_3.grid(row=0, column=1, padx=2)

        lista = tk.Listbox(submenu, width=80, height=25, selectmode="single")

        def buscar(var):
            tutor = funciones.Tutor.buscarTutores(var)
            lista.delete(0, tk.END)
            if tutor:
                for tuto in tutor:
                    opc = f"{tuto[1]:<25} | {tuto[0]:<50}"
                    lista.insert(tk.END, opc)
            lista.pack(pady=5)
            return tutor

        tutores = buscar("")

        tk.Button(
            frame_busqueda,
            image=button_image_3,
            command=lambda: buscar(id_psi, buscador.get()),
            bg="#ffffff",
            borderwidth=0
        ).grid(row=0, column=1, padx=2)

        frame_botones = tk.Frame(submenu, bg="#ffffff")
        frame_botones.pack(pady=20)

        def Aceptar():
            try:
                indice = lista.curselection()[0]
                val = tutores[indice]
                submenu.resultado = val
            except:
                submenu.resultado = None
            submenu.destroy()

        tk.Button(
            frame_botones,
            text="Seleccionar",
            command=Aceptar
        ).grid(row=0, column=0, padx=20)

        tk.Button(
            frame_botones,
            text="Cancelar",
            command=lambda: submenu.destroy()
        ).grid(row=0, column=1, padx=20)

        # ✅ Esperar a que el submenú se cierre
        submenu.resultado = None
        submenu.wait_window()

        return submenu.resultado

    @staticmethod
    def subGrupos(ventana, id_psi):
        submenu = tk.Toplevel(ventana, width=400, height=300, bg="#ffffff")
        submenu.title("Grupos")

        buscador = tk.StringVar()

        frame_busqueda = tk.Frame(submenu, bg="#ffffff")
        frame_busqueda.pack(pady=5)

        txt_buscador = tk.Entry(frame_busqueda, textvariable=buscador, width=40)
        txt_buscador.grid(row=0, column=0, padx=2)

        path = os.path.abspath("img/")
        button_image_3 = PhotoImage(file=path + "/search.png")
        # botón de búsqueda (solo uno)
        button_3 = tk.Button(
            frame_busqueda,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: buscar(buscador.get()),
            relief="flat",
            bg="#ffffff"
        )
        button_3.image = button_image_3
        button_3.grid(row=0, column=1, padx=2)

        lista = tk.Listbox(submenu, width=80, height=25, selectmode="single")
        lista.pack(pady=5)

        grupos = []  # lista que se actualizará

        def buscar(var):
            nonlocal grupos
            grupos = funciones.Grupo.buscarGrupo(var)
            lista.delete(0, tk.END)
            if grupos:
                for grup in grupos:
                    opc = f"{grup[2]} {grup[3]} {grup[4]} {grup[1]}"
                    lista.insert(tk.END, opc)

            return grupos

        # búsqueda inicial
        buscar("")


        frame_botones = tk.Frame(submenu, bg="#ffffff")
        frame_botones.pack(pady=20)

        def Aceptar():
            try:
                indice = lista.curselection()[0]
                submenu.resultado = grupos[indice]
            except:
                submenu.resultado = None
            submenu.destroy()

        boton1=tk.Button(frame_botones, text="Seleccionar", command=Aceptar).grid(row=0, column=0, padx=20)
        boton2=tk.Button(frame_botones, text="Cancelar", command=lambda: submenu.destroy()).grid(row=0, column=1, padx=20)

        submenu.resultado = None
        submenu.wait_window()

        return submenu.resultado

    @staticmethod
    def subCalendario(ventana):
        submenu = tk.Toplevel(ventana)
        submenu.title("Calendario")
        submenu.config(bg="#ffffff")

        # Fecha actual
        hoy = datetime.today().date()

        # Crear calendario
        cal = Calendar(
            submenu,
            selectmode="day",
            year=hoy.year,
            month=hoy.month,
            day=hoy.day,
            date_pattern="yyyy-mm-dd"
        )
        cal.pack(pady=20)

        # Frame de botones
        frame_botones = tk.Frame(submenu, bg="#ffffff")
        frame_botones.pack(pady=20)

        # Botón aceptar
        def Aceptar():
            submenu.resultado = cal.get_date()   # ← aquí guardas la fecha seleccionada
            submenu.destroy()

        tk.Button(
            frame_botones,
            text="Seleccionar",
            command=Aceptar
        ).grid(row=0, column=0, padx=20)

        # Botón cancelar
        tk.Button(
            frame_botones,
            text="Cancelar",
            command=lambda: submenu.destroy()
        ).grid(row=0, column=1, padx=20)

        # Valor por defecto
        submenu.resultado = None

        # Esperar a que se cierre
        submenu.wait_window()

        return submenu.resultado
