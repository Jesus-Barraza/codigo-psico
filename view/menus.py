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
        container=ft.Container(
            ft.Column(
                [
                    ft.Image(
                        src="logo_psicopedagogia_v2.svg",
                        width=200,
                        height=200,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Bienvenido al Programa de\nPsicopedagogía",
                        size=40,
                        color="#034748",
                        font_family="Jaques_Francois",
                        text_align="center",
                    ),
                    ft.ElevatedButton(
                        text="Iniciar sesión",
                        width=200,
                        height=60,
                        bgcolor="#D9D9D9",
                        color="#000000",
                        on_click=lambda:print("Iniciar sesión"),
                    ),
                    ft.ElevatedButton(
                        text="Registrarse",
                        width=200,
                        height=60,
                        bgcolor="#D9D9D9",
                        color="#000000",
                        on_click=lambda:print("Iniciar sesión"),
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
            ),
            width=1920,
            height=1080,

        )
        ventana.add(container)
        ventana.update()