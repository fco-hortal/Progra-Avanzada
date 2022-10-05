from cargar import cargar_archivos
from os import path
from collections import deque


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = set()
        # self.seguidores = [] # almacenar a los seguidores es opcional.


class Pintogram:
    def __init__(self):
        self.dic_usuarios = dict()

    def nuevo_usuario(self, id_usuario, nombre):
        usuario = Usuario(id_usuario, nombre)
        self.dic_usuarios[id_usuario] = usuario

    def follow(self, id_seguidor, id_seguido):
        self.dic_usuarios[id_seguidor].seguidos.add(self.dic_usuarios[id_seguido])

    def cargar_red(self, ruta_red):
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.
        f = cargar_archivos(ruta_red)
        for i in f:
            self.nuevo_usuario(i[0], i[1])
        f = cargar_archivos(ruta_red)
        for i in f:
            for j in i[2]:
                self.follow(i[0], j)



    def unfollow(self, id_seguidor, id_seguido):
        self.dic_usuarios[id_seguidor].seguidos.remove(self.dic_usuarios[id_seguido])

    def mis_seguidos(self, id_usuario):
        return len(self.dic_usuarios[id_usuario].seguidos)





    def distancia_social(self, id_usuario_1, id_usuario_2):
        # Método que retorna la "distancia social" de dos usuarios
        visitados = []
        # La cola de siempre, comienza desde el nodo inicio.
        queue = deque(self.dic_usuarios[id_usuario_1].seguidos)

        while len(queue) > 0:
            vertice = queue.popleft()
            # Detalle clave: si ya visitamos el nodo, no hacemos nada!
            if vertice not in visitados:
                visitados.append(vertice)
                # Agregamos los vecinos a la cola si es que no han sido visitados.
                for vecino in self.dic_usuarios[vertice].id:
                    if vecino not in visitados:
                        queue.add(vecino)
        return visitados


if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
#    print(pintogram.distancia_social("3", "5"))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
