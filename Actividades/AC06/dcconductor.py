import csv
from conductores import Conductor
from excepcion_patente import ErrorPatente
import os

class DCConductor:

    def __init__(self, registro_oficial, conductores):
        '''
        El constructor crea las estructuras necesarias para almacenar los datos
         proporcionados, recibe la información necesaria para el funcionamiento de la clase.
        '''
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()


    def chequear_rut(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su rut no siga
        el formato correcto
        '''
        if len(conductor.rut) > 10:
            raise TypeError('No lleva puntos')
        if len(conductor.rut) < 10:
            raise TypeError('lleva guion')



    def chequear_nombre(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su nombre no
        exista en el registro oficial.
        '''
        if conductor.nombre not in self.registro_oficial:
            raise TypeError(f'No se encuentra a {conductor.nombre} en el registro')



    def chequear_celular(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su celular
        no siga el formato correcto
        '''
        if conductor.celular.isnumeric() == False:
            raise TypeError('Se necesitan solo numeros')
        if len(str(conductor.celular)) != 9:
            raise TypeError('Mas de 9 numeros')
        if conductor.celular[0] != '9':
            raise TypeError('No comienza con 9')



    def chequear_patente(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su patente no
        coincida con la información del registro oficial.
        '''
        if conductor.patente not in self.registro_oficial[conductor.nombre]:
            raise ErrorPatente('La patente no esta en el registro')

