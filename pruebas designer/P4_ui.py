import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class gui(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("P4.ui", self)
        self.contador = 0
        self.pushButton.clicked.connect(self.contar)


    def contar(self):
        self.contador += 1
        print(f'{self.contador} Clicks')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = gui()
    GUI.show()
    sys.exit(app.exec_())

 