
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QProgressBar,  QPushButton)
import os
from PyQt5.QtGui import (QPixmap)

#   Se utilizo la actividad 05 y los contenidos de la semana 06-07 para realizar estas clases
class Ventana_inicio(QWidget):
    senal_abrir_ventana = pyqtSignal(str)  # abre la ventana del juego

    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.setGeometry(700, 300, 500, 400)
        self.setWindowTitle('Inicio DCClub')

        self.texto_ingreso = QLabel('Ingresa nombre de usurio:', self)
        self.input_usuario = QLineEdit()
        self.boton_ingresar = QPushButton('Ingresar', self)
        self.boton_ingresar.clicked.connect(self.button_ingresar_pressed)
        # self.boton_jugar.clicked.connect(Campo.abrir_otra_ventana)

        self.mensaje_error = QLabel('', self)
        self.logo = QLabel()
        ruta_logo = os.path.join('sprites/personajes', 'logo.png')
        pixeles = QPixmap(ruta_logo)
        # Agregamos los pixeles al elemento QLabel
        self.logo.setPixmap(pixeles)
        # Finalmente, ajustamos tamaño de contenido al tamaño del elemento (100 x 100)
        self.logo.setScaledContents(True)

        col = QVBoxLayout()
        col.addStretch(1)
        col.addWidget(self.logo)
        col.addWidget(self.texto_ingreso)
        col.addWidget(self.input_usuario)
        col.addWidget(self.boton_ingresar)
        col.addWidget(self.mensaje_error)
        col.addStretch(1)
        hbox = QHBoxLayout()
        hbox.addLayout(col)
        self.setLayout(hbox)

    def button_ingresar_pressed(self):
        texto = self.input_usuario.text()
        self.senal_abrir_ventana.emit(texto)

    def archivo_erroneo(self, filename):
        self.mensaje_error.setText(f"usuario - {filename} - no encontrado")

    def cerrar_ventana(self, filename):
        self.hide()

class Ventana_principal(QWidget):

    def __init__(self):
        super().__init__()

    def inicializa_gui(self):
        self.setGeometry(700, 300, 700, 700)
        self.setWindowTitle('DCClub')

        self.fondo = QLabel()
        ruta_fondo = os.path.join('sprites/fondos', '1.png')
        pixeles = QPixmap(ruta_fondo)
        # Agregamos los pixeles al elemento QLabel
        self.fondo.setPixmap(pixeles)
        # Finalmente, ajustamos tamaño de contenido al tamaño del elemento (100 x 100)
        self.fondo.setScaledContents(True)



