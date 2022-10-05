"""
Aquí debes completar las funciones de las consultas
"""


def resumen_actual(ayudantes, alumnos):
    num_alumnos = len(alumnos)
    num_ayudantes = len(ayudantes)
    piso_1 = len(ayudantes.keys("Nuevos"))
    piso_2 = len(ayudantes.keys("Mentores"))
    piso_3 = len(ayudantes.keys("Jefes"))
    piso_4 = len(ayudantes.keys("Chief Tamburini"))
    print(f"Alumnos restantes: {num_alumnos}")
    print(f"Ayudantes restantes: {num_ayudantes})
    print(f"Piso -1: {piso_1}")
    print(f"Piso -2: {piso_2}")
    print(f"Piso -3: {piso_3}")
    print(f"Piso -4: {piso_4}")
def stock_comida(alumnos):
    #return tuple(comida, len(key(comida))
    pass
