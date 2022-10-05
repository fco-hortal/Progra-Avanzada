from PyQt5.QtCore import QObject, pyqtSignal, QRect, QThread
import os
from parametros_generales import N
import time


class Campo(QObject):
    senal_archivo_erroneo = pyqtSignal(str)
    senal_enviar_posiciones = pyqtSignal(list)  # abre la ventana del juego

    def __init__(self):
        super().__init__()

        self.archivo = ''

    def abrir_otra_ventana(self):
        # Si tenemos una señal asociada para abrir otra ventana
        if self.senal_abrir_otra_ventana:
            # Ocultamos esta ventana y emitimos la señal para abrir otra
            # self.hide()
            self.senal_abrir_otra_ventana.emit()
            self.abrir_archivo()

    def abrir_archivo(self, file_name):

        x = os.path.exists(f'mapas/{file_name}')
        if x:
            with open(f'mapas/{file_name}', 'r') as f:
                try:
                    lista1 = f.readlines()
                    lista2 = []
                    for i in lista1:
                        lista2.append(i.strip().split(' '))

                    f.close()
                    self.senal_enviar_posiciones.emit(lista2)
                except(RuntimeError, TypeError, NameError) as e:
                    # Si ocurre cualquier error con el archivo se printea error
                    print(e)
        else:
            self.senal_archivo_erroneo.emit(file_name)

        # si archivo no es vaido o no existe

        #


#   Sacado de Ayudantia 5 2018 SS
class Character(QObject):
    update_position_signal = pyqtSignal(dict)

    def __init__(self, x, y):
        super().__init__()
        self.direction = 'R'
        self._x = x
        self._y = y
        self.i = N
        self.j = N

        # Se conecta la señal update_position con el metodo del parent
        # (Ventana_juego.update_position)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """
        Chequea que y este dentro de los parametros y envía la señal update_position al cambiar la
        coordenada y.
        :param value: int
        :return: none
        """
        if 0 < value < N * self.i:
            self._y = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        """
        Chequea que la coordenada x  se encuentre dentro de los parámetros y envía la señal
        update_position con las nuevas coordenadas.
        :param value: int
        :return: none
        """
        if 0 < value < N * self.j:
            self._x = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})

    def move(self, event):
        """
        Función que maneja los eventos de movimiento (L, R, U, D).
        :param event: dict
        :return: none
        """
        self.i = event['I']
        self.j = event['J']
        # hitbox_personaje = QRect(self.x + 1, self.y + 1, N, N)

        if event['posicion'] == 'R':
            self.x += 10
            self.direction = 'R'
        if event['posicion'] == 'L':
            self.x -= 10
            self.direction = 'L'
        if event['posicion'] == 'U':
            self.y -= 10
            self.direction = 'U'
        if event['posicion'] == 'D':
            self.y += 10
            self.direction = 'D'


class Time(QThread):
    tiempo_senal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.dia = 0
        self.hora = 0
        self.minuto = 0

    def run(self):
        cont = 0
        diccionario = {1: self.minuto, 2: self.hora, 3: self.dia}
        while True:
            cont += 1
            time.sleep(0.5)
            if cont < 60:
                self.minuto = cont
                self.tiempo_senal.emit(diccionario)
            else:
                self.hora += 1
                cont = 0
                self.tiempo_senal.emit(diccionario)
                if self.hora >= 24:
                    self.dia += 1
                    self.hora = 0
                    self.tiempo_senal.emit(diccionario)


