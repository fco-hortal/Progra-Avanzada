import random
import parametros as p


class Vehiculo:
    def __init__(self, juego):
        self.juego = juego
        self.nombre = None
        self.dueno = None
        self.categoria = None
        self.chasis = None
        self.carroceria = None
        self.ruedas = None
        self.motor_zapatillas = None
        self.peso = None
        self.precio = None
        self.mejoras = []

    def rellenar_vehiculos_inicio(self):
        if self.categoria == "automóvil":
            self.chasis = random.randint(p.AUTOMOVIL['CHASIS']['MIN'],
                                         p.AUTOMOVIL['CHASIS']['MAX'] + 1)
            self.carroceria = random.randint(p.AUTOMOVIL['CARROCERIA']['MIN'],
                                             p.AUTOMOVIL['CARROCERIA']['MAX'] + 1)
            self.ruedas = random.randint(p.AUTOMOVIL['RUEDAS']['MIN'],
                                         p.AUTOMOVIL['RUEDAS']['MAX'] + 1)
            self.motor_zapatillas = random.randint(p.AUTOMOVIL['MOTOR']['MIN'],
                                                   p.AUTOMOVIL['MOTOR']['MAX'] + 1)
            self.peso = random.randint(p.AUTOMOVIL['PESO']['MIN'], p.AUTOMOVIL['PESO']['MAX'] + 1)
            print(self.peso)
        elif self.categoria == "troncomóvil":
            self.chasis = random.randint(p.TRONCOMOVIL['CHASIS']['MIN'],
                                         p.TRONCOMOVIL['CHASIS']['MAX'] + 1)
            self.carroceria = random.randint(p.TRONCOMOVIL['CARROCERIA']['MIN'],
                                             p.TRONCOMOVIL['CARROCERIA']['MAX'] + 1)
            self.ruedas = random.randint(p.TRONCOMOVIL['RUEDAS']['MIN'],
                                         p.TRONCOMOVIL['RUEDAS']['MAX'] + 1)
            self.motor_zapatillas = random.randint(p.TRONCOMOVIL['ZAPATILLAS']['MIN'],
                                                   p.TRONCOMOVIL['ZAPATILLAS']['MAX'] + 1)
            self.peso = random.randint(p.TRONCOMOVIL['PESO']['MIN'],
                                       p.TRONCOMOVIL['PESO']['MAX'] + 1)

        elif self.categoria == "bicicleta":
            self.chasis = random.randint(p.BICICLETA['CHASIS']['MIN'],
                                         p.BICICLETA['CHASIS']['MAX'] + 1)
            self.carroceria = random.randint(p.BICICLETA['CARROCERIA']['MIN'],
                                             p.BICICLETA['CARROCERIA']['MAX'] + 1)
            self.ruedas = random.randint(p.BICICLETA['RUEDAS']['MIN'],
                                         p.BICICLETA['RUEDAS']['MAX'] + 1)
            self.motor_zapatillas = random.randint(p.BICICLETA['ZAPATILLAS']['MIN'],
                                                   p.BICICLETA['ZAPATILLAS']['MAX'] + 1)
            self.peso = random.randint(p.TRONCOMOVIL['PESO']['MIN'], p.BICICLETA['PESO']['MAX'] + 1)

        elif self.categoria == "motocicleta":
            self.chasis = random.randint(p.MOTOCICLETA['CHASIS']['MIN'],
                                         p.MOTOCICLETA['CHASIS']['MAX'] + 1)
            self.carroceria = random.randint(p.MOTOCICLETA['CARROCERIA']['MIN'],
                                             p.MOTOCICLETA['CARROCERIA']['MAX'] + 1)
            self.ruedas = random.randint(p.MOTOCICLETA['RUEDAS']['MIN'],
                                         p.MOTOCICLETA['RUEDAS']['MAX'] + 1)
            self.motor_zapatillas = random.randint(p.MOTOCICLETA['MOTOR']['MIN'],
                                                   p.MOTOCICLETA['MOTOR']['MAX'] + 1)
            self.peso = random.randint(p.MOTOCICLETA['PESO']['MIN'],
                                       p.MOTOCICLETA['PESO']['MAX'] + 1)

