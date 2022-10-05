from ventanas import Ventana_inicio
from PyQt5.QtWidgets import (QApplication)
import sys

if __name__ == '__main__':

    app = QApplication([])

    # Se crea el Front-end
    ventana_inicio = Ventana_inicio()

    ventana_inicio.show()

    sys.exit(app.exec_())