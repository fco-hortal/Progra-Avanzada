from carga_archivos import cargar_datos
from dcconductor import DCConductor
from excepcion_patente import ErrorPatente

'''
Para cada uno de los conductores chequea si su información está correcta.
Si no está correcta, se informa en pantalla que el conductor no pudo ser
registrado y la razón, y si no, se informa que fue inscrito exitosamente.
En este archivo la idea es capturar y manejar las excepciones.
También deberás contar la cantidad total de errores.
'''

try:
    registro_oficial, conductores = cargar_datos("regiztro_ofizial.json", "conductores.csv")
except FileNotFoundError as error:
    print(f'No se encontro el archivo {error.filename}')

try:
    registro_oficial, conductores = cargar_datos("registro_oficial.json", "conductores.csv")
except FileNotFoundError as error:
    print(f'No se encontro el archivo {error.filename}')

dcconductor = DCConductor(registro_oficial, conductores)

'''
Editar desde aquí
'''
if registro_oficial and conductores:
    contador = 0

    for conductor in dcconductor.conductores:
        try:
            dcconductor.chequear_celular(conductor)
            dcconductor.chequear_rut(conductor)
            dcconductor.chequear_nombre(conductor)
            dcconductor.chequear_patente(conductor)
            dcconductor.seleccionados.append(conductor)

        except TypeError as error:
            print(error)
            contador+=1
        except ErrorPatente as error:
            print(error)
            contador+=1

    print(contador)