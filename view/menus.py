import flet as ft
from threading import Timer
import re

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


    def validar_registro(self):
        nombre = self.nombre.value.strip()
        correo = self.correo.value.strip()
        telefono = self.telefono.value.strip()
        contra = self.contrasena.value.strip()
        confirmar = self.confirmar.value.strip()

        # 1. Campos vacíos
        if not nombre or not correo or not telefono or not contra or not confirmar:
            self.lbl_error.value = "Todos los campos son obligatorios."
            return False

        # 2. Validar correo
        regex_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(regex_correo, correo):
            self.lbl_error.value = "El correo electrónico no es válido."
            return False

        # 3. Validar teléfono
        if not telefono.isdigit() or len(telefono) < 8:
            self.lbl_error.value = "El número telefónico debe contener solo números y mínimo 8 dígitos."
            return False

        # 4. Validar contraseña mínima
        if len(contra) < 8:
            self.lbl_error.value = "La contraseña debe tener al menos 8 caracteres."
            return False

        # 5. Contraseñas iguales
        if contra != confirmar:
            self.lbl_error.value = "Las contraseñas no coinciden."
            return False

        # Si todo está bien
        self.lbl_error.value = ""
        return True


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
        
        # Top decoration
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
                            on_click=lambda e:self.menuRegistrarse(ventana),
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

        # Bottom decoration
        bottom_decoration = ft.Container(
            content=ft.Image(
                src="esquina1.svg",
                width=500,
                height=700,
                fit=ft.ImageFit.CONTAIN,
            ),
            margin=ft.margin.only(left=-200, bottom=-300),
            alignment=ft.alignment.bottom_left,
            disabled=True,
        )

        # Main content with overlay decoration
        main_content = ft.Stack(
            controls=[
                bottom_decoration,  # atrás
                top_row,
                main_column,        # adelante
            ]
        )
        
        # Container with main content
        container = ft.Container(
            content=main_content,
            width=1920,
            height=1080,
            bgcolor="#BCDFE6",
        )
        
        ventana.add(container)
        ventana.update()
    
    def menuIniciarSesion(self, ventana):
        ventana.controls.clear()
        self.fontFamily(ventana)

        # ------------------------------
        # FUNCIONES DE VISUALIZAR/Ocultar contraseña
        # ------------------------------
        def toggle_password(e):
            self.contrasena.password = not self.contrasena.password
            password_icon.icon = ft.Icons.VISIBILITY if self.contrasena.password else ft.Icons.VISIBILITY_OFF
            ventana.update()

        def toggle_password2(e):
            self.confirmar.password = not self.confirmar.password
            password2_icon.icon = ft.Icons.VISIBILITY if self.confirmar.password else ft.Icons.VISIBILITY_OFF
            ventana.update()

        # ------------------------------
        # CAMPOS DE FORMULARIO
        # ------------------------------
        input_style = dict(
            width=600,
            height=55,
            bgcolor="#EFE8E8",
            border_radius=12,
            content_padding=ft.padding.symmetric(horizontal=15, vertical=10)
        )

        self.nombre = ft.TextField(label="", hint_text="", **input_style)

        self.correo = ft.TextField(label="", hint_text="", **input_style)

        self.telefono = ft.TextField(label="", hint_text="", **input_style)

        self.contrasena = ft.TextField(
            label="", 
            hint_text="", 
            password=True, 
            can_reveal_password=False,
            **input_style
        )

        self.confirmar = ft.TextField(
            label="", 
            hint_text="", 
            password=True, 
            can_reveal_password=False,
            **input_style
        )

        self.lbl_error = ft.Text(
            value="",
            color="red",
            size=14,
            weight=ft.FontWeight.BOLD
        )

        def registrar_click(self, e):
            if self.validar_registro():
                print("Registro válido, continuar...")
                # Aquí haces INSERT a BD o cambias de pantalla
            else:
                self.page.update()


        # Botones de mostrar/ocultar
        password_icon = ft.IconButton(
            icon=ft.Icons.VISIBILITY,
            on_click=toggle_password,
        )
        password2_icon = ft.IconButton(
            icon=ft.Icons.VISIBILITY_OFF,
            on_click=toggle_password2,
        )

        # ------------------------------
        # FORM CON ÍCONOS AL ESTILO DE LA IMAGEN
        # ------------------------------
        def labeled(icon, text):
            return ft.Row(
                controls=[
                    ft.Icon(icon, size=28, color="black"),
                    ft.Text(text, size=20, weight="bold", font_family="Jaques_Francois")
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )

        form = ft.Column(
            [
                ft.Row([ft.Image(src="logo_psicopedagogia_v2.svg", width=120)], alignment="center"),

                ft.Text(
                    "Iniciar sesión",
                    size=40,
                    weight="w900",
                    font_family="Jaques_Francois",
                    text_align="center"
                ),

                # ----------- CORREO ----------
                labeled(ft.Icons.EMAIL, "Correo electrónico:"),
                self.correo,

                # ----------- CONTRASEÑA ----------
                labeled(ft.Icons.KEY, "Contraseña:"),
                ft.Row([self.contrasena, password_icon], alignment="center"),

                ft.Container(height=20),

                # BOTÓN REGISTRAR
                ft.ElevatedButton(
                    text="Registrar",
                    width=200,
                    height=50,
                    color="black",
                    bgcolor="#EDEDED",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        side=ft.BorderSide(2, "black"),
                        text_style=ft.TextStyle(
                            size=20,
                            weight="w500",
                            font_family="Jaques_Francois",
                        )
                    )
                ),

                ft.Container(height=15),

                # ENLACE INICIAR SESIÓN
                ft.Row([
                    ft.Text("¿No tienes una cuenta?  "),
                    ft.TextButton(
                        "Regístrate aquí",
                        style=ft.ButtonStyle(
                            color=ft.Colors.BLUE,
                        ),
                        on_click=lambda e: self.menuRegistrarse(ventana)
                    )
                ], alignment="center"),

            ],
            spacing=15,
            horizontal_alignment="center",
            alignment="center"
        )
        # Bottom decoration
        bottom_decoration = ft.Container(
            content=ft.Image(
                src="esquina1.svg",
                width=500,
                height=700,
                fit=ft.ImageFit.CONTAIN,
            ),
            margin=ft.margin.only(left=-200, bottom=-300),
            alignment=ft.alignment.bottom_left,
            disabled=True,
        )

        # Top decoration
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

        main_content = ft.Stack(
            controls=[
                bottom_decoration,  # atrás
                top_row,
                form,        # adelante
            ]
        )

        # --------------- DECORACIONES ---------------
        decor = ft.Stack(
            [
                ft.Container(content=main_content, alignment=ft.alignment.center)
            ],
            expand=True
        )

        ventana.add(decor)
        ventana.update()


    def menuRegistrarse(self, ventana):
        ventana.controls.clear()
        self.fontFamily(ventana)

        # ------------------------------
        # FUNCIONES DE VISUALIZAR/Ocultar contraseña
        # ------------------------------
        def toggle_password(e):
            self.contrasena.password = not self.contrasena.password
            password_icon.icon = ft.Icons.VISIBILITY if self.contrasena.password else ft.Icons.VISIBILITY_OFF
            ventana.update()

        def toggle_password2(e):
            self.confirmar.password = not self.confirmar.password
            password2_icon.icon = ft.Icons.VISIBILITY if self.confirmar.password else ft.Icons.VISIBILITY_OFF
            ventana.update()

        # ------------------------------
        # CAMPOS DE FORMULARIO
        # ------------------------------
        input_style = dict(
            width=600,
            height=55,
            bgcolor="#EFE8E8",
            border_radius=12,
            content_padding=ft.padding.symmetric(horizontal=15, vertical=10)
        )

        self.nombre = ft.TextField(label="", hint_text="", **input_style)

        self.correo = ft.TextField(label="", hint_text="", **input_style)

        self.telefono = ft.TextField(label="", hint_text="", **input_style)

        self.contrasena = ft.TextField(
            label="", 
            hint_text="", 
            password=True, 
            can_reveal_password=False,
            **input_style
        )

        self.confirmar = ft.TextField(
            label="", 
            hint_text="", 
            password=True, 
            can_reveal_password=False,
            **input_style
        )

        self.lbl_error = ft.Text(
            value="",
            color="red",
            size=14,
            weight=ft.FontWeight.BOLD
        )

        def registrar_click(self, e):
            if self.validar_registro():
                print("Registro válido, continuar...")
                # Aquí haces INSERT a BD o cambias de pantalla
            else:
                self.page.update()

        # Botones de mostrar/ocultar
        password_icon = ft.IconButton(
            icon=ft.Icons.VISIBILITY,
            on_click=toggle_password,
        )
        password2_icon = ft.IconButton(
            icon=ft.Icons.VISIBILITY_OFF,
            on_click=toggle_password2,
        )

        # ------------------------------
        # FORM CON ÍCONOS AL ESTILO DE LA IMAGEN
        # ------------------------------
        def labeled(icon, text):
            return ft.Row(
                controls=[
                    ft.Icon(icon, size=28, color="black"),
                    ft.Text(text, size=20, weight="bold", font_family="Jaques_Francois")
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )

        form = ft.Column(
            [
                ft.Row([ft.Image(src="logo_psicopedagogia_v2.svg", width=120)], alignment="center"),

                ft.Text(
                    "Registrar nuevo usuario",
                    size=40,
                    weight="w900",
                    font_family="Jaques_Francois",
                    text_align="center"
                ),

                # ----------- NOMBRE ----------
                labeled(ft.Icons.ACCOUNT_CIRCLE, "Nombre:"),
                self.nombre,

                # ----------- CORREO ----------
                labeled(ft.Icons.EMAIL, "Correo electrónico:"),
                self.correo,

                # ----------- TELÉFONO ----------
                labeled(ft.Icons.PHONE, "Número telefónico:"),
                self.telefono,

                # ----------- CONTRASEÑA ----------
                labeled(ft.Icons.KEY, "Contraseña:"),
                ft.Row([self.contrasena, password_icon], alignment="center"),

                # ----------- CONFIRMAR CONTRA ----------
                ft.Text(
                    "Confirmar contraseña:",
                    size=20,
                    weight="bold",
                    font_family="Jaques_Francois",
                ),
                ft.Row([self.confirmar, password2_icon], alignment="center"),

                ft.Container(height=20),

                # BOTÓN REGISTRAR
                ft.ElevatedButton(
                    text="Registrar",
                    width=200,
                    height=50,
                    color="black",
                    bgcolor="#EDEDED",
                    on_click=registrar_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        side=ft.BorderSide(2, "black"),
                        text_style=ft.TextStyle(
                            size=20,
                            weight="w500",
                            font_family="Jaques_Francois",
                        )
                    )
                ),

                ft.Container(height=15),

                # ENLACE INICIAR SESIÓN
                ft.Row([
                    ft.Text("¿Ya tienes una cuenta?  "),
                    ft.TextButton(
                        "Inicie sesión aquí",
                        style=ft.ButtonStyle(
                            color=ft.Colors.BLUE,
                        ),
                        on_click=lambda e: self.menuIniciarSesion(ventana)
                    )
                ], alignment="center"),

            ],
            spacing=15,
            horizontal_alignment="center",
            alignment="center"
        )
        
        # Bottom decoration
        bottom_decoration = ft.Container(
            content=ft.Image(
                src="esquina1.svg",
                width=500,
                height=700,
                fit=ft.ImageFit.CONTAIN,
            ),
            margin=ft.margin.only(left=-200, bottom=-300),
            alignment=ft.alignment.bottom_left,
            disabled=True,
        )

        # Top decoration
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

        main_content = ft.Stack(
            controls=[
                bottom_decoration,  # atrás
                top_row,
                form,        # adelante
            ]
        )

        # --------------- DECORACIONES ---------------
        decor = ft.Stack(
            [
                ft.Container(content=main_content, alignment=ft.alignment.center)
            ],
            expand=True
        )

        ft.Column([
            self.nombre,
            self.correo,
            self.telefono,
            self.contrasena,
            self.confirmar,
            self.lbl_error,     # ← aquí aparece el error
            ft.ElevatedButton("Registrar", on_click=registrar_click)
        ])


        ventana.add(decor)
        ventana.update()
