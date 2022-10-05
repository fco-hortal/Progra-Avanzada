from ventanas import Ventana_inicio, Ventana_juego
from dccampo import Campo, Character, Time
from PyQt5.QtWidgets import (QApplication)
from parametros_generales import N
import sys

if __name__ == '__main__':

    app = QApplication([])

    # Se crea el Front-end
    ventana_inicio = Ventana_inicio()
    ventana_juego = Ventana_juego()
    campo = Campo()
    personaje = Character(N, N)
    tiempo = Time()

    tiempo.tiempo_senal.connect(ventana_juego.set_time)
    ventana_inicio.senal_abrir_ventana.connect(campo.abrir_archivo)

    ventana_juego.move_character_signal.connect(personaje.move)
    # Con esta también vinculamos a ventana 1 desde ventana 2
    campo.senal_enviar_posiciones.connect(ventana_juego.inicializa_gui)
    campo.senal_enviar_posiciones.connect(ventana_inicio.cerrar_ventana)
    campo.senal_archivo_erroneo.connect(ventana_inicio.archivo_erroneo)

    personaje.update_position_signal.connect(ventana_juego.update_position)

    ventana_inicio.show()

    sys.exit(app.exec_())

    #def iteracion_de_tiempo():

