'''
Este es un archivo temporal en lo que se realizan las demás instancias.
Por lo pronto esto representarán los acomodos exactos del menú y funciones básicas
'''

import os

class App():
    def __init__(self):
        self.menuInicioSesion()
    
    @staticmethod
    def borrarPantalla():
        os.system("cls")

    @staticmethod
    def esperarTecla():
        input("Presiona enter para continuar")

    def menuInicioSesion(self):
        self.borrarPantalla()
        opc=True
        while opc:
            print("inicio de sesion y contraseña")
            opc=input("Elije tu opción \n1- Inicio de sesión \n2- Registro \n3- Salir \n (1-3):").strip()
            match opc:
                case "1":
                    self.borrarPantalla()
                    self.inicio_sesion()
                case "2":
                    self.borrarPantalla()
                    self.registrar()
                case "3":
                    opc=False
                    print("Terminó la ejecución del sistema")
                case _:
                    opc=True
                    self.borrarPantalla()
                    print("Opción no válida")

    def inicio_sesion(self):
        print("inicio de sesion")
        correo=input("correo electronico: ").strip
        contra=input("contraseña: ").strip
        if correo=="nosexd@gmail.com" and contra=="1234":
            self.main()

    def registrar(self):
        nombre=input("Ingrese su nombre")
        correo=input("Ingrese el correo electrónico")
        contraseña=input("Ingrese su contraseña")
        self.main()

    def menuCitas(self):
        print("Menu de citas")
        print(f"| {'nombre del estudiante':<50} | {'fecha':<20} | {'prioridad':10} | {'n° de cita':<20} | {'status':<50}")
        print("no hay citas por el momento")
        self.esperarTecla()
        self.main()

    def calendario(self):
        print("calendario de citas")
        print("No hay citas registradas por el momento")
        self.esperarTecla()
        self.main()

    def Notificaciones(self):
        print("Menú de notificaciones")
        print("No hay notificaciones nuevas por el momento")
        self.esperarTecla()
        self.main()

    def configuracion(self):
        print("configuracion")
        print("Nota de creador: el menú no es funcional dado a que no hay funciones importantes que mencionar")
        self.esperarTecla()
        self.main()
    
    def main(self):
        self.borrarPantalla()
        opc=True
        while opc:
            print("Menú inicial")
            opc=input("Elige una opcion: \n1.-Menú de citas \n2.-Calendario \n3.-Notificaciones \n4.-Configuración \n5.-Salir \n (1-5):").strip()
            match opc:
                case "1":
                    self.borrarPantalla()
                    self.menuCitas()
                case "2":
                    self.borrarPantalla()
                    self.calendario()
                case "3":
                    self.borrarPantalla()
                    self.Notificaciones()
                case "4":
                    self.borrarPantalla()
                    self.configuracion()
                case "5":
                    print("Volviendo al inicio de sesion")
                    self.menuInicioSesion()
                case "_":
                    opc=True
                    self.borrarPantalla()
                    print("Opción no válida, inténtelo de nuevo")

if __name__ == "__main__":
    a=App()