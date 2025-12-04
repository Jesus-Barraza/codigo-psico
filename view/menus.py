import flet as ft
from threading import Timer

#Clase para el menú principal
class Menu():
    #Configuración inicial de la ventana
    def __init__(self, ventana):
        ventana.title = "Programa de Psicopedagogía" #Título
        ventana.theme_mode = ft.ThemeMode.LIGHT #Modo de tema claro
        ventana.vertical_alignment = "center"
        ventana.horizontal_alignment = "center" #Alineación centrada
        ventana.resizable = False #No redimensionable
        ventana.window_width = 1920
        ventana.window_height = 1080 #Tamaño de ventana
        ventana.bgcolor = "#BCDFE6" #Color de fondo
        ventana.update() #Actualizar ventana
        self.pantallaCarga(ventana) 

    #Fuentes de texto como función
    @staticmethod
    def fontFamily(ventana):
        ventana.fonts = {
            "Jaques_Francois": "fonts/jaques_francois/JacquesFrancois-Regular.ttf"
        }

    #Pantalla de carga inicial
    def pantallaCarga(self, ventana):
        #Limpiar controles y mostrar imagen de carga
        ventana.controls.clear()
        imagen = ft.Image(
            src="logo_psicopedagogia_v2.svg",
            width=600,
            height=600,
            fit=ft.ImageFit.CONTAIN,
        )
        ventana.add(imagen)
        ventana.update()
        #Temporizador para cambiar a menú de inicio
        start=Timer(3.0, lambda:self.menuInicio(ventana))
        start.start()

    def menuInicio(self, ventana):
        ventana.controls.clear()
        self.fontFamily(ventana)
        # Some Flet versions don't include Positioned; use Rows/Columns instead
        top_row = ft.Row(
            [
                ft.Container(expand=True),
                ft.Container(
                    content=ft.Image(
                        src="esquina2.svg",
                        width=500,
                        height=500,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    margin=ft.margin.only(top=-200, right=-200),
                    alignment=ft.alignment.top_right,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

        bottom_row = ft.Row(
            [
                ft.Container(
                    content=ft.Image(
                        src="esquina1.svg",
                        width=500,
                        height=700,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    margin=ft.margin.only(left=-200, bottom=-300),
                    alignment=ft.alignment.bottom_left,
                ),
                ft.Container(expand=True),
            ]
            ,
            vertical_alignment=ft.CrossAxisAlignment.END,
        )

        main_column = ft.Column(
            [
                ft.Container(
                    ft.Column([
                        ft.Image(
                            src="logo_psicopedagogia_v2.svg",
                            width=200,
                            height=200,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Text(
                            "Bienvenido al programa de\nPsicopedagogía",
                            size=40,
                            color="#034748",
                            font_family="Jaques_Francois",
                            text_align="center",
                            weight="w900",
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Column([
                        ft.ElevatedButton(
                            text="Iniciar sesión",
                            width=200,
                            height=60,
                            bgcolor="#D9D9D9",
                            color="#000000",
                            on_click=lambda e: self.menuIniciarSesion(ventana),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                side=ft.BorderSide(1, "#000000"),
                                text_style=ft.TextStyle(
                                    weight="w400",
                                    font_family="Jaques_Francois",
                                    size=20,
                                ),
                            ),
                        ),
                        ft.ElevatedButton(
                            text="Registrarse",
                            width=200,
                            height=60,
                            bgcolor="#D9D9D9",
                            color="#000000",
                            on_click=lambda e: self.menuRegistrarse(ventana),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                side=ft.BorderSide(1, "#000000"),
                                text_style=ft.TextStyle(
                                    weight="w400",
                                    font_family="Jaques_Francois",
                                    size=20,
                                ),
                            ),
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

        container = ft.Container(
            content=ft.Column([top_row, main_column, bottom_row], expand=True),
            width=1920,
            height=1080,
            bgcolor="#BCDFE6",
        )
        ventana.add(container)
        ventana.update()
    
    def menuIniciarSesion(self, ventana):
        ventana.controls.clear()
        ventana.update()

    def menuRegistrarse(self, ventana):
        ventana.controls.clear()
        ventana.update()