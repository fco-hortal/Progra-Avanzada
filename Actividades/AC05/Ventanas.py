from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
import os

"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.

Eres libre de agregar otras clases si lo crees conveniente.
"""

class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Este método inicializa la interfaz y todos sus widgets.
        """

        # Ajustamos la geometría de la ventana y su título
        self.setGeometry(200, 100, 1000, 400)
        self.setWindowTitle('Colgado')

        self.palabra_completandose = QLabel('Palabra', self)

        self.usadas = QLabel("", self)
        self.disponibles = QLabel(f'Disponibles: ', self)

        self.mensaje = QLabel('', self)
        self.letra = QLabel('Letra:', self)
        self.boton_sl = QPushButton('Seleccionar Letra', self)
        self.boton_nj = QPushButton('Nuevo Juego', self)

        self.imagen = QLabel()
        ruta_imagen = os.path.join('images', '1.png')
        pixeles = QPixmap(ruta_imagen)
        # Agregamos los pixeles al elemento QLabel
        self.imagen.setPixmap(pixeles)

        # Finalmente, ajustamos tamaño de contenido al tamaño del elemento (100 x 100)
        self.imagen.setScaledContents(True)

        columna1 = QVBoxLayout()
        columna1.addStretch(1)
        columna1.addWidget(self.palabra_completandose)
        columna1.addWidget(self.mensaje)
        columna1.addWidget(self.letra)
        columna1.addWidget(self.boton_sl)
        columna1.addWidget(self.boton_nj)

        columna2 = QVBoxLayout()
        columna2.addStretch(1)
        columna2.addWidget(self.imagen)
        columna2.addWidget(self.disponibles)
        columna2.addWidget(self.usadas)

        hbox = QHBoxLayout()
        hbox.addLayout(columna1)
        hbox.addLayout(columna2)
        self.setLayout(hbox)

    def keyPressEvent(self, event):
        self.letra.setText(f'Letra: {event.text()}')
        dic = {"letra": event.text()}
        self.enviar_letra_signal.emit(dic)

    def recibidor_mensajes(self, diccionario):
        print(diccionario)
        self.mensaje.setText(diccionario['msg'])
        self.usadas.setText(diccionario['usadas'])
        self.disponibles.setText(diccionario['disponibles'])
        self.palabra_completandose.setText(diccionario['palabra'])
        pixeles = QPixmap(diccionario['imagen'])
        # Agregamos los pixeles al elemento QLabel
        self.imagen.setPixmap(pixeles)
