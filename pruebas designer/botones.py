import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QGridLayout, QVBoxLayout)

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.label1 = QLabel('Status:', self)
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '0', 'CE', 'C']

        posiciones = [(i, j) for i in range(4) for j in range(3)]

        for posicion, valor in zip(posiciones, valores):
            boton = QPushButton(valor, self)

            """
            Aquí conectamos el evento clicked() de cada boton con el slot
            correspondiente. En este ejemplo todos los botones usan el
            mismo slot (self.boton_clickeado).
            """
            boton.clicked.connect(self.boton_clickeado)

            self.grilla.addWidget(boton, *posicion)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Calculator')

    def boton_clickeado(self):
        """
        Esta función se ejecuta cada vez que uno de los botones de la grilla
        es presionado. Cada vez que el botón genera el evento, la función inspecciona
        cual botón fue presionado y recupera la posición en que se encuentra en
        la grilla.
        """

        # Sender retorna el objeto que fue clickeado.
        # Ahora, la variable boton referencia una instancia de QPushButton
        boton = self.sender()

        # Obtenemos el identificador del elemento en la grilla
        idx = self.grilla.indexOf(boton)

        # Con el identificador obtenemos la posición del ítem en la grilla
        posicion = self.grilla.getItemPosition(idx)

        # Actualizamos label1
        self.label1.setText(f'Status: Presionado boton {idx}, en fila/columna: {posicion[:2]}.')

if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())
