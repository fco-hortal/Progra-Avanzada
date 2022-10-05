import os
import json
import time # Ocupe time.strftime para obtener fecha y hora


class DocengelionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Docengelion):
            return {'modelo': obj.modelo,
                    'estado': 'reparacion',
                    'registro_reparacion': time.strftime("%b %d %Y %H:%M:%S"),
                    'nucleo': obj.nucleo}

            # Mantenemos la serialización por defecto para otros tipos
        return super().default(obj)

class Docengelion:
    def __init__(self, modelo, nucleo, *args, **kwargs):
        self.modelo = modelo
        self.nucleo = nucleo
        self.estado = 'funcional'
        self.registro_reparacion = None


def recibir_eva(ruta):
    with open(ruta, "r") as archivo:
        lista_d = []
        lista = json.load(archivo)
        for i in lista:
            a = Docengelion(**i)
            lista_d.append(a)


        return lista_d


def reparar_eva(docengelion):
    json.dump(docengelion)


if __name__ == '__main__':
    try:
        dcngelions = recibir_eva('docent.json')
        if dcngelions:
            print("DANIAR200: Ha cargado las unidades Docengelion")
        try:
            for unidad in dcngelions:
                reparar_eva(unidad)
            print("DANIAR201: Se estan reparando las unidades Docengelion")
        except Exception as error:
            print(f'Error: {error}')
            print("DANIAR501: No ha podido reparar las unidades Docengelion")
    except Exception as error:
        print(f'Error: {error}')
        print("DANIAR404: No ha podido cargar las unidades Docengelion")

    print(dcngelions)

