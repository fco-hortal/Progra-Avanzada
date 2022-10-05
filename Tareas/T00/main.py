import parametros
import tablero
import random
import celda


def menu_1():
    # crear partida

    nom_usuario = input("Nombre de usuario: ")

    largo_t = int(input("Largo tablero: "))

    n_posibles = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    if largo_t not in n_posibles:
        print('Se requiere un numero entero del 3 al 15')
        largo_t = int(input("Largo tablero: "))

    ancho_t = int(input("Ancho tablero: "))
    if ancho_t not in n_posibles:
        print("Se requiere un numero entero del 3 al 15")
        ancho_t = int(input("Ancho tablero: "))

    return largo_t, ancho_t, nom_usuario


def cantidad_legos(largo_t, ancho_t):
    n_legos = round(largo_t * ancho_t * parametros.PROB_LEGO)
    return n_legos


def descubrir_bomba(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[j][i].bomba:
                t[j][i].bombas_cercanas = "L"
    tablero.print_tablero_sin_utf8(lista_para_imprimir(t))

    print("Perdiste", nom_usuario, ":(")


def calcular_puntaje(n_legos, celdas_descubiertas, POND_PUNT):
    puntaje = n_legos * celdas_descubiertas * POND_PUNT
    ranking = open("puntaje.txt", "a")
    ranking.write(str(puntaje) + "\n")
    return puntaje


# proximas 3 funciones sacadas de https://www.youtube.com/watch?v=5d1CfnYT-KM&list=PLyqJaJwNMikB-nNOcVdSik-KbB5EWgjI9

def n_bombas_cercanas(t, x, y):
    s = 0
    for (x1, y1) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if corrobador(int(x) + x1, int(y) + y1):
            if t[int(x) + x1][int(y) + y1].bomba:
                s += 1

    if s >= 0:
        t[y][x].bombas_cercanas = s


def corrobador(x, y):
    if x >= 0 and x < ancho_tablero and y >= 0 and y < largo_tablero:
        return True
    return False


def generador_tablero(largo_t, ancho_t, n_legos):
    t = []
    for i in range(largo_t):
        t.append([])
        for j in range(ancho_t):
            t[i].append(celda.Celda())
    # El proximo loop fue ideado gracias a https://www.youtube.com/watch?v=5d1CfnYT-KM
    for i in range(n_legos):
        while True:
            x = random.randint(-1, ancho_t - 1)
            y = random.randint(-1, largo_t - 1)
            if not t[y][x].bomba:
                t[y][x].bomba = True
                break

    for i in range(len(t)):
        for j in range(len(t[i])):
            t[i][j].cx = j
            t[i][j].cy = i

    return t


def lista_para_imprimir(t):
    lista = []
    for i in range(len(t)):
        l = []
        for j in range(len(t[i])):
            l.append(t[i][j].bombas_cercanas)
        lista.append(l)
    return lista


opcion_inicial = int(input("Seleccione una opcion: \n [1] Crear partida \n [2] Cargar partida \n [3] Ver ranking "
                           "\n [0] Salir \n \n Indique su opcion (0, 1, 2 o 3):"))

if opcion_inicial == 1:
    largo_tablero, ancho_tablero, nom_usuario = menu_1()
    n_legos = cantidad_legos(largo_tablero, ancho_tablero)

    t = generador_tablero(largo_tablero, ancho_tablero, n_legos)

    for i in range(largo_tablero * ancho_tablero + 1000):
        celdas_descubiertas = 0
        tablero.print_tablero_sin_utf8(lista_para_imprimir(t))
        x = int(input("Coordenada x: "))
        y = int(input("Coordenada y: "))
        celdas_descubiertas += 1
        n_bombas_cercanas(t, x, y)

        if t[y][x].bomba:
            descubrir_bomba(t)
            puntaje = calcular_puntaje(n_legos, celdas_descubiertas, parametros.POND_PUNT)
            print("Puntaje:", puntaje)
            break

        if celdas_descubiertas == largo_tablero * ancho_tablero - n_legos:
            print("Felicidades", nom_usuario, "Ganaste!")
            puntaje = calcular_puntaje(n_legos, celdas_descubiertas, parametros.POND_PUNT)
            print("Puntaje:", puntaje)
            break

elif opcion_inicial == 2:
    # cargar partida
    nom_usuario = input("Nombre de usuario:")

elif opcion_inicial == 3:
    # ver ranking
    ranking = open("puntaje.txt", "r")
    lista_puntajes = []
    for i in ranking:
        lista_puntajes.append(int(i.strip()))
    lista_puntajes.sort(reverse=True)
    for i in range(10):
        print(lista_puntajes[i])
    opcion_inicial = int(input("Seleccione una opcion: \n [1] Crear partida \n [2] Cargar partida \n [3] Ver ranking "
                               "\n [0] Salir \n \n Indique su opcion (0, 1, 2 o 3):"))

elif opcion_inicial == 0:
    True

else:
    print("opcion no valida")
    opcion_inicial = int(input("Seleccione una opcion: \n [1] Crear partida \n [2] Cargar partida \n [3] Ver ranking "
                               "\n [0] Salir \n \n Indique su opcion (0, 1, 2 o 3):"))
