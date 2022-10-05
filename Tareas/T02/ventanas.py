
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QProgressBar,  QPushButton)
import os
from PyQt5.QtGui import (QPixmap)
from parametros_generales import (celdas_mapa, N, ENERGIA_JUGADOR,
                                  ESPACIO_EXTRA_I, ESPACIO_EXTRA_J, PAGINA,
                                  DIA, HORA, DINERO)


#   Se utilizo la actividad 05 y los contenidos de la semana 06-07 para realizar estas clases
class Ventana_inicio(QWidget):
    senal_abrir_ventana = pyqtSignal(str)  # abre la ventana del juego
    senal_lista_obstaculos = pyqtSignal(list)  # trate de poner choque
    senal_inicio_horario = pyqtSignal()  # trate de poner el tiempo

    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.setGeometry(700, 300, 500, 400)
        self.setWindowTitle('Inicio DCCampo')

        self.texto_ingreso = QLabel('Ingresa el nombre del mapa a cargar:', self)
        self.input_mapa = QLineEdit()
        self.boton_jugar = QPushButton('Jugar', self)
        self.boton_jugar.clicked.connect(self.button_jugar_pressed)
        # self.boton_jugar.clicked.connect(Campo.abrir_otra_ventana)

        self.mensaje_error = QLabel('', self)
        self.imagen = QLabel()
        ruta_imagen = os.path.join('sprites/otros', 'logo.png')
        pixeles = QPixmap(ruta_imagen)
        # Agregamos los pixeles al elemento QLabel
        self.imagen.setPixmap(pixeles)
        # Finalmente, ajustamos tamaño de contenido al tamaño del elemento (100 x 100)
        self.imagen.setScaledContents(True)

        col = QVBoxLayout()
        col.addStretch(1)
        col.addWidget(self.imagen)
        col.addWidget(self.texto_ingreso)
        col.addWidget(self.input_mapa)
        col.addWidget(self.boton_jugar)
        col.addWidget(self.mensaje_error)
        col.addStretch(1)
        hbox = QHBoxLayout()
        hbox.addLayout(col)
        self.setLayout(hbox)

    def button_jugar_pressed(self):
        texto = self.input_mapa.text()
        self.senal_abrir_ventana.emit(texto)

    def archivo_erroneo(self, filename):
        self.mensaje_error.setText(f"archivo - {filename} - no encontrado")

    def cerrar_ventana(self, filename):
        self.hide()
    def iniciar_tiempo(self):
        self.senal_inicio_horario.emit()


class Ventana_juego(QWidget):
    # Sacado de ayudantia 5 SS 2018
    move_character_signal = pyqtSignal(dict)  # Envia los movimientos

    def __init__(self):
        super().__init__()
        lista = []

    def inicializa_gui(self, lista2):

        self.setWindowTitle('Juego DCCampo')

        #       inventario
        self.paginas = QLabel(f'Pagina: {PAGINA}', self)
        self.img_inventario = QLabel('Completar', self)
        self.boton_regreso = QPushButton('<--', self)
        self.boton_siguiente = QPushButton('-->', self)

        #       estadisticas
        self.titulo_stats = QLabel('Stats', self)
        self.tx_dia = QLabel(f'Dia: {DIA}', self)
        self.tx_hr = QLabel(f'Hr: {HORA}')
        self.tx_dinero = QLabel(f'$: {DINERO}', self)
        self.tx_energia = QLabel(f'Energia: {ENERGIA_JUGADOR}', self)

        self.barra_progreso = QProgressBar(self)
        self.barra_progreso.setSizePolicy(300, 25)
        self.barra_progreso.setMaximum(ENERGIA_JUGADOR)
        self.barra_progreso.setValue(ENERGIA_JUGADOR)

        self.boton_pausar = QPushButton('Pausar', self)

        self.boton_salir = QPushButton('Salir', self)

        #       mapa

        inventario = QHBoxLayout()
        inventario.addStretch(1)
        inventario.addWidget(self.paginas)
        inventario.addWidget(self.img_inventario)
        inventario.addWidget(self.boton_regreso)
        inventario.addWidget(self.boton_siguiente)
        inventario.addStretch(1)

        estadisticas = QVBoxLayout()
        estadisticas.addStretch(2)
        estadisticas.addWidget(self.titulo_stats)
        estadisticas.addWidget(self.tx_dia)
        estadisticas.addWidget(self.tx_hr)
        estadisticas.addWidget(self.tx_dinero)
        estadisticas.addWidget(self.tx_energia)
        estadisticas.addWidget(self.barra_progreso)
        estadisticas.addWidget(self.boton_pausar)
        estadisticas.addWidget(self.boton_salir)
        estadisticas.addStretch(2)

        cont1 = 0
        cont2 = 0
        self.conti = len(lista2)
        self.contj = len(lista2[0])
        self.lista_obstaculos = []
        for i in range(len(lista2)):
            for j in range(len(lista2[i])):
                if lista2[i][j] == 'O':
                    img_mapa = QLabel('', self)
                    ruta1_imagen = os.path.join(celdas_mapa['espacio_libre'] + '.png')
                    pixeles1 = QPixmap(ruta1_imagen)
                    img_mapa.setPixmap(pixeles1.scaled(N, N))
                    img_mapa.setGeometry(j * N, i * N, N, N)

                elif lista2[i][j] == 'C':
                    img_mapa = QLabel('', self)
                    ruta1_imagen = os.path.join(celdas_mapa['espacio_cultivable'] + '.png')
                    pixeles1 = QPixmap(ruta1_imagen)
                    img_mapa.setPixmap(pixeles1.scaled(N, N))
                    img_mapa.setGeometry(j * N, i * N, N, N)

                elif lista2[i][j] == 'R':
                    img1_mapa = QLabel('', self)
                    img_mapa = QLabel('', self)
                    ruta2_imagen = os.path.join(celdas_mapa['espacio_libre'] + '.png')
                    pixeles1 = QPixmap(ruta2_imagen)
                    img1_mapa.setPixmap(pixeles1.scaled(N, N))
                    img1_mapa.setGeometry(j * N, i * N, N, N)

                    ruta1_imagen = os.path.join(celdas_mapa['roca'] + '.png')
                    pixeles1 = QPixmap(ruta1_imagen)
                    img_mapa.setPixmap(pixeles1.scaled(N, N))
                    img_mapa.setGeometry(j * N, i * N, N, N)
                    obs = QRect(j * N, i * N, N, N)
                    self.lista_obstaculos.append(obs)

                elif lista2[i][j] == 'H':
                    img1_mapa = QLabel('', self)
                    ruta2_imagen = os.path.join(celdas_mapa['espacio_libre'] + '.png')
                    pixeles1 = QPixmap(ruta2_imagen)
                    img1_mapa.setPixmap(pixeles1.scaled(N, N))
                    img1_mapa.setGeometry(j * N, i * N, N, N)
                    cont1 += 1
                    if cont1 == 4:
                        img_mapa = QLabel('', self)
                        ruta1_imagen = os.path.join(celdas_mapa['casa'] + '.png')
                        pixeles1 = QPixmap(ruta1_imagen)
                        img_mapa.setPixmap(pixeles1.scaled(2 * N, 2 * N))
                        img_mapa.setGeometry((j - 1) * N, (i - 1) * N, 2 * N, 2 * N)
                        cont1 += 1
                elif lista2[i][j] == 'T':
                    img1_mapa = QLabel('', self)
                    ruta2_imagen = os.path.join(celdas_mapa['espacio_libre'] + '.png')
                    pixeles1 = QPixmap(ruta2_imagen)
                    img1_mapa.setPixmap(pixeles1.scaled(N, N))
                    img1_mapa.setGeometry(j * N, i * N, N, N)
                    cont2 += 1
                    if cont2 == 4:
                        img_mapa = QLabel('', self)
                        ruta1_imagen = os.path.join(celdas_mapa['tienda'] + '.png')
                        pixeles1 = QPixmap(ruta1_imagen)
                        img_mapa.setPixmap(pixeles1.scaled(2 * N, 2 * N))
                        img_mapa.setGeometry((j - 1) * N, (i - 1) * N, 2 * N, 2 * N)

        self._frame = 1

        self.front_character = QLabel(self)
        self.front_character.setPixmap(QPixmap('sprites/personaje/right_1.png'))
        self.front_character.move(N, N)

        self.setGeometry(700, 200, self.contj * N + ESPACIO_EXTRA_J, self.conti * N +
                         ESPACIO_EXTRA_I)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(inventario)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addLayout(estadisticas)

        self.setLayout(hbox)
        self.show()

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if value > 3:
            self._frame = 1
        else:
            self._frame = value

    def keyPressEvent(self, e):
        """
        Dada la presión de una tecla se llama a esta función. Al apretarse una tecla chequeamos si
        esta dentro de las teclas del control del juego y de ser así, se envía una señal al backend
        con la acción además de actualizar el sprite.
        :param e: QKeyEvent
        :return:
        """
        self.frame += 1
        if e.key() == Qt.Key_D:
            self.front_character.setPixmap(QPixmap(f'sprites/personaje/right_{self.frame}.png'))
            self.move_character_signal.emit({'posicion': 'R', 'I': self.conti, 'J': self.contj,
                                             'L': self.lista_obstaculos})
        if e.key() == Qt.Key_A:
            self.front_character.setPixmap(QPixmap(f'sprites/personaje/left_{self.frame}.png'))
            self.move_character_signal.emit({'posicion': 'L', 'I': self.conti, 'J': self.contj,
                                             'L': self.lista_obstaculos})
        if e.key() == Qt.Key_W:
            self.front_character.setPixmap(
                QPixmap(f'sprites/personaje/up_{self.frame}.png'))
            self.move_character_signal.emit({'posicion': 'U', 'I': self.conti, 'J': self.contj,
                                             'L': self.lista_obstaculos})
        if e.key() == Qt.Key_S:
            self.front_character.setPixmap(
                QPixmap(f'sprites/personaje/down_{self.frame}.png'))
            self.move_character_signal.emit({'posicion': 'D', 'I': self.conti, 'J': self.contj,
                                             'L': self.lista_obstaculos})

    def update_position(self, event):
        """
        Función que recibe un diccionario con las cordenadas del personaje y las actualiza en el
        frontend.
        :param event: dict
        :return: none
        """
        self.front_character.move(event['x'], event['y'])

    def set_time(self, event):
        self.tx_hr.setText(f'Hr: {event[1]}:{event[2]}')
        self.tx_dia.setText(f'Dia: {event[3]}')

