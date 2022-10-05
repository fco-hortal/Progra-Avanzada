"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""

from collections import deque
"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    cola = []
    h = open(ruta_archivo_alumnos, "r", encoding='utf-8')

    for x in h.readlines():
        x = x.strip()
        x = x.split(";")
        x[1] = x[1].split(",")
        cola.append(x)

    return cola


    h.close()



def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    # Completar
    h = open(ruta_archivo_ayudantes, "r", encoding='utf-8')
    list = []
    dic_ayudantes = dict()
    for x in h.readlines():
        x = x.strip()
        x = x.split(";")
        dic_ayudantes[x[0]] = x[1]


    return dic_ayudantes

    h.close()


