from abc import abstractmethod
import funciones as f

@abstractmethod
class Menus:
    def __init__(self, juego):
        self.juego = juego
        pass

    def siguiente_menu(self, tipo_menu):
        siguiente = self.juego.menus[tipo_menu]
        return siguiente

    def volver(self, tipo_menu):
        atras = self.juego.menus[tipo_menu]
        return atras

    #   funcion sacada de: https://www.youtube.com/watch?v=Xf-WAYytfKo


class MenuSesion(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    def pedir_nombre(self):
        nombre_usuario = input("Cree un nombre de usuario:")
        if nombre_usuario.isalnum():
            return nombre_usuario
        else:
            print("nombre no valido, ocupar caracteres"
                  " alfanumericos y no repetir usuarios\n")
            self.pedir_nombre()

    def elegir_equipo(self):
        print("\nElija un equipo\n1)Tareos\n"
              "2)Hibridos\n3)Docencios\n")
        equipo = input("Respuesta:")
        if equipo == "1":
            return "Tareos"
        elif equipo == "2":
            return "Hibridos"
        elif equipo == "3":
            return "Docencios"
        else:
            print("opcion no valida")
            self.elegir_equipo()

    def elegir_vehiculo(self):
        print("Elija un vehiculo para comenzar la carrera\n")
        print("1) Automovil \n2) Troncomovil \n3) Bicicleta \n4) Motocicleta\n")
        vehiculo = input("Respuesta:")
        tipo_vehiculo = None
        if vehiculo == "1":
            tipo_vehiculo = "automóvil"
        elif vehiculo == "2":
            tipo_vehiculo = "troncomóvil"
        elif vehiculo == "3":
            tipo_vehiculo = "bicicleta"
        elif vehiculo == "4":
            tipo_vehiculo = "motocicleta"
        else:
            print("nombre no valido, ocupar caracteres"
                  " alfanumericos y no repetir nombres de auto\n")
            self.elegir_vehiculo()
        return tipo_vehiculo

    def nombre_vehiculo(self):
        nombre_vehiculo = input("Nombre del vehiculo:")
        if nombre_vehiculo.isalnum():
            return nombre_vehiculo
        else:
            self.nombre_vehiculo()

    def recibir_input(self):
        print("Bienvenido! Por favor elija una opcion \n")
        print("1) Crear nueva partida \n2) Cargar una partida existente \n" +
              "0) Salir \n")
        respuesta = input("Respuesta:")

        if respuesta == "0":
            return False
        elif respuesta == "1":
            #   crear nueva partida
            nombre_usuario = self.pedir_nombre()
            equipo = self.elegir_equipo()
            tipo_vehiculo = self.elegir_vehiculo()
            nombre_vehiculo = self.nombre_vehiculo()
            #   agregando el input a los objetos
            self.juego.piloto.nombre = nombre_usuario
            self.juego.piloto.equipo = equipo
            self.juego.vehiculo.nombre = nombre_vehiculo
            self.juego.vehiculo.categoria = tipo_vehiculo
            #   agregando el resto de parametros a los objetos
            self.juego.piloto.rellenar_piloto_inicio()
            self.juego.vehiculo.rellenar_vehiculos_inicio()

            self.siguiente_menu("Principal").recibir_input()

        elif respuesta == "2":
            # cargar partida existente
            self.siguiente_menu("Principal").recibir_input()

        else:
            print("Respuesta no valida\n")
            self.recibir_input()


class MenuPrincipal(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    # pedir una opcion y entregar el numero de la opcion que eligio el usuario
    def recibir_input(self):
        print("\nElija una opcion\n")
        print(
            "1) Comprar nuevos vehiculos \n" + "2) Iniciar una carrera \n" + "3) Volver atras \n" +
            "0) Salir \n" + "9) Guardar la partida\n")
        respuesta = input("Respuesta:")
        if respuesta == "0":
            return False
        elif respuesta == "1":
            # crear nueva partida
            self.siguiente_menu("Compra").recibir_input()
        elif respuesta == "2":
            # cargar partida existente
            self.siguiente_menu("Pistas").recibir_input()
        elif respuesta == "3":
            self.volver("Sesion").recibir_input()
        elif respuesta == "9":
            f.guardar_jugador("pilotos.csv", self.juego.piloto.nombre, self.juego.piloto.dinero,
                              self.juego.piloto.personalidad, self.juego.piloto.contextura,
                              self.juego.piloto.equilibrio, self.juego.piloto.experiencia,
                              self.juego.piloto.equipo)
            f.guardar_vehiculo("vehículos.csv", self.juego.vehiculo.nombre,
                               self.juego.vehiculo.dueno, self.juego.vehiculo.categoria,
                               self.juego.vehiculo.chasis, self.juego.vehiculo.carroceria,
                               self.juego.vehiculo.ruedas, self.juego.vehiculo.motor_zapatillas,
                               self.juego.vehiculo.peso)
            print("Partida guardada!")
            self.volver("Sesion").recibir_input()
        else:
            print("Respuesta no valida\n")
            self.recibir_input()


class MenuCarrera(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    def recibir_input(self):
        print("\nElija una opcion\n")
        print("1) Crear nueva partida \n" + "2) Cargar una partida existente \n" +
              "0) Salir \n" + "9) Volver atras\n")
        respuesta = input("Respuesta:")
        if respuesta == 0:
            return False
        elif respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 9:
            pass
        else:
            print("Respuesta no valida")
            self.recibir_input()


class MenuPits(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    def recibir_input(self):
        print(f"\nDinero actual: ${self.juego.jugador.dinero}\n")
        print("Partes a mejorar: \n")
        """Mostrar opciones de mejoras segun el vehiculo que se
            este ocupando con el precio"""
        if respuesta == 0:
            return False
        elif respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            pass
        elif respuesta == 4:
            pass
        else:
            print("Respuesta no valida\n")
            self.recibir_input()


class MenuCompra(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    # pedir una opcion y entregar el numero de la opcion que eligio el usuario
    def recibir_input(self):
        print(f"\nDinero actual: ${self.juego.jugador.dinero}\n")
        print("Vehiculos disponibles para comprar: \n" + "1) Automovil  $1.500 \n" +
              "2) Troncomovil   $600 \n" + "3) Motocicleta  $1.100 \n" +
              "4) Bicicleta $500 \n" + "0) Salir \n" + "9) Volver a menu de inicio \n")
        respuesta = input("Respuesta:")
        if respuesta == 0:
            return False
        elif respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            pass
        elif respuesta == 4:
            pass
        elif respuesta == "9":
            self.volver("Principal").recibir_input()
        else:
            print("Respuesta no valida")
            self.recibir_input()


class MenuPistas(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    def recibir_input(self):
        print("\nSeleccione pista:\n")
        print("1) Pista de hielo \n" + "2) Pista rocosa \n" +
              "3) Pista suprema \n" + "4) Volver atras\n" + "0) Salir \n")
        respuesta1 = input("Respuesta:")
        if respuesta1 in ["1", "2", "3"]:
            self.siguiente_menu("Vehiculos").recibir_input()
        elif respuesta1 == "0":
            return
        elif respuesta1 == "4":
            self.volver("Principal").recibir_input()
        else:
            print("Respuesta no valida\n")
            self.recibir_input()


class MenuVehiculos(Menus):
    def __init__(self, juego):
        super().__init__(juego)

    def recibir_input(self):
        print("\nSeleccione vehiculo:\n")
        # recorre los vehiculos que tiene el jugador y los da como opciones
        for i in range(len(self.juego.jugador.vehiculos)):
            print(f"{i}) {self.juego.jugador.vehiculos[i].nombre} \n")
            print("0) Salir /n")
        respuesta2 = input("Respuesta:")
        if respuesta2 in [0, 1, 2, 3, 4]:
            return respuesta2
        else:
            print("Respuesta no valida\n")
            self.recibir_input()
