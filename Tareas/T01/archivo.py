from menus import MenuSesion, MenuPrincipal, MenuCarrera, MenuPits, MenuCompra, MenuPistas, \
    MenuVehiculos
from jugador import Jugador
from pilotos import Piloto
from vehiculo import Vehiculo
from pistas import Pista


# import funciones as f

class Juego:
    def __init__(self):
        self.piloto = Piloto(self)
        self.vehiculo = Vehiculo(self)
        self.jugador = Jugador(self)
        self.pista = Pista()
        self.menus = {
            "Sesion": MenuSesion(self),
            "Principal": MenuPrincipal(self),
            "Carrera": MenuCarrera(self),
            "Pits": MenuPits(self),
            "Compra": MenuCompra(self),
            "Pistas": MenuPistas(self),
            "Vehiculos": MenuVehiculos(self)
        }

    def crear_partida(self):
        pass

    def cargar_partida(self):
        pass


j = Juego()
pil = j.piloto
v = j.vehiculo
ju = j.jugador
pi = j.pista

j.menus['Sesion'].recibir_input()
