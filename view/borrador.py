import tkinter as tk
from tkinter import messagebox,  Canvas, PhotoImage
from pathlib import Path
from controller import funciones
import os
from . import menus
import flet as ft
import multiprocessing

class Volver():
    def __init__(self, ventana):
        menus.Menu(ventana)

def iniciarFlet():
    ft.app(target=Volver, assets_dir="img", view=ft.AppView.FLET_APP)

class Menu():
    def __init__(self, ventana, sesion):
        ventana.geometry("1920x1080")
        ventana.title("Programa de psicopedagogía")   
        ventana.config(bg="#FAFAFA")  
        self.menuPrincipal(ventana, sesion)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def grupoTitulo(self, ventana, texto, color1, color2):
        # Frame superior
        frame_superior = tk.Frame(ventana, bg=color1, height=200)
        frame_superior.pack(fill="x", side="top")

        # Frame contenedor horizontal
        frame_horizontal = tk.Frame(frame_superior, bg=color1)
        frame_horizontal.pack(fill="x", padx=10, pady=10)

        frame_horizontal.columnconfigure(0, weight=1)  # espacio a la izquierda
        frame_horizontal.columnconfigure(1, weight=0)  # título centrado
        frame_horizontal.columnconfigure(2, weight=1)

        # Frame del título (izquierda)
        frame_titulo = tk.Frame(frame_horizontal, bg=color2, height=30, width=400)
        frame_titulo.grid(row=0, column=1, padx=10)

        lbl_titulo = tk.Label(frame_titulo, text=texto, font=("Arial", 24), fg="black", bg=color2)
        lbl_titulo.pack(anchor="center")

        # Frame de botones (derecha)
        frame_botones = tk.Frame(frame_horizontal, bg=color1)
        frame_botones.grid(row=0, column=2, sticky="e")

        path = os.path.abspath("img/")
        self.button_image_1 = PhotoImage(file=path + "/config.png")
        button_1 = tk.Button(
            frame_botones,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat",
            bg=color1
        )
        button_1.pack(side="left", padx=10)

        self.button_image_2 = PhotoImage(file=path + "/noti.png")
        button_2 = tk.Button(
            frame_botones,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat",
            bg=color1
        )
        button_2.pack(side="left", padx=10)

    def submenu(self,ventana, sesion):
        #funcion
        def cerrarSesion(ventana):
            ventana.destroy()
            p = multiprocessing.Process(target=iniciarFlet)
            p.start()

        #Barra del menú
        menubar=tk.Menu(ventana, bg="#5E95D4", fg="white")
        ventana.config(menu=menubar)

        #Archivo del menú
        menuarch=tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Menú desplegable", menu=menuarch)
        menuarch.add_command(label="Menú principal", command=lambda:self.menuPrincipal(ventana, sesion))
        menuarch.add_command(label="Calendario", command=lambda:None)
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
        self.grupoTitulo(ventana, "Menú principal", "#5E95D4", "#D9D9D9")

        #Cuadro de citas del día
        lbl_citas_dia = tk.Label(ventana, text="Citas activas", font=("Arial", 18), fg="black", bg="#D9D9D9")
        lbl_citas_dia.pack(pady=10)

        frame_citas_dia = tk.Frame(ventana, bg="#FFFFFF", height=200, width=600, relief="raised", bd=2)
        frame_citas_dia.pack(pady=20)

        citas_dia=funciones.Citas.obtener_citas_dia(sesion[0])   
        if len(citas_dia) > 0:
            lbl_titulo_citas_0=tk.Label(frame_citas_dia, text="Cita ID", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_0.grid(row=0, column=0, pady=10, padx=5)

            lbl_titulo_citas_1=tk.Label(frame_citas_dia, text="Nombre del alumno", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_1.grid(row=0, column=1, pady=10, padx=5)

            lbl_titulo_citas_2=tk.Label(frame_citas_dia, text="Fecha", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_2.grid(row=0, column=2, pady=10, padx=5)

            lbl_titulo_citas_3=tk.Label(frame_citas_dia, text="Status", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_3.grid(row=0, column=3, pady=10, padx=5)
            num_citas=1

            for cita in citas_dia:
                lbl_cita_0 = tk.Label(frame_citas_dia, text=f"{cita[0]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_0.grid(row=num_citas, column=0, pady=5)

                lbl_cita_1 = tk.Label(frame_citas_dia, text=f"{cita[1]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_1.grid(row=num_citas, column=1, pady=5)

                lbl_cita_2 = tk.Label(frame_citas_dia, text=f"{cita[2]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_2.grid(row=num_citas, column=2, pady=5)

                lbl_cita_3 = tk.Label(frame_citas_dia, text=f"{cita[3]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_3.grid(row=num_citas, column=3, pady=5)

                num_citas += 1
        else:
            lbl_no_citas=tk.Label(frame_citas_dia, text="Por lo pronto, no se han realizado citas", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_no_citas.pack(pady=10)

            btn_interaccion=tk.Button(
                frame_citas_dia,
                text="Agregar cita",
                font=("Arial", 14, "underline"),
                fg="blue",
                bg="white",
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
                command=lambda:None
            )
            btn_interaccion.pack(pady=10)

        #Cuadro de citas pasadas
        lbl_citas_h = tk.Label(ventana, text="Citas activas", font=("Arial", 18), fg="black", bg="#D9D9D9")
        lbl_citas_h.pack(pady=10)

        frame_citas_h = tk.Frame(ventana, bg="#FFFFFF", height=200, width=600, relief="raised", bd=2)
        frame_citas_h.pack(pady=20)

        citas_dia=funciones.Citas.obtener_citas_h(sesion[0])   
        if len(citas_dia) > 0:
            lbl_titulo_citas_0=tk.Label(frame_citas_h, text="Cita ID", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_0.grid(row=0, column=0, pady=10, padx=5)

            lbl_titulo_citas_1=tk.Label(frame_citas_h, text="Nombre del alumno", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_1.grid(row=0, column=1, pady=10, padx=5)

            lbl_titulo_citas_2=tk.Label(frame_citas_h, text="Fecha", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_2.grid(row=0, column=2, pady=10, padx=5)

            lbl_titulo_citas_3=tk.Label(frame_citas_h, text="Status", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_titulo_citas_3.grid(row=0, column=3, pady=10, padx=5)
            num_citas=1

            for cita in citas_dia:
                lbl_cita_0 = tk.Label(frame_citas_h, text=f"{cita[0]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_0.grid(row=num_citas, column=0, pady=5)

                lbl_cita_1 = tk.Label(frame_citas_h, text=f"{cita[1]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_1.grid(row=num_citas, column=1, pady=5)

                lbl_cita_2 = tk.Label(frame_citas_h, text=f"{cita[2]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_2.grid(row=num_citas, column=2, pady=5)

                lbl_cita_3 = tk.Label(frame_citas_h, text=f"{cita[3]}", font=("Arial", 12), fg="black", bg="#FFFFFF")
                lbl_cita_3.grid(row=num_citas, column=3, pady=5)

                num_citas += 1
        else:
            lbl_no_citas=tk.Label(frame_citas_h, text="No han habido citas recientes", font=("Arial", 16), fg="black", bg="#FFFFFF")
            lbl_no_citas.pack(pady=10)