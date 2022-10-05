import parametros as p
import csv


# Info: https://www.programiz.com/python-programming/working-csv-files
# funciones para el guardado de la partida
def guardar_jugador(file_path, nombre, dinero, personalidad, contextura, equilibrio,
                    experiencia, equipo):
    fieldnames = [nombre, dinero, personalidad, contextura, equilibrio, experiencia, equipo]

    with open(file_path, "a") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(fieldnames)
    csvFile.close()


def guardar_vehiculo(file_path, nombre, dueno, categoria, chasis, carroceria,
                     ruedas, motor_zapatillas, peso):
    fieldnames = [nombre, dueno, categoria, chasis, carroceria,
                  ruedas, motor_zapatillas, peso]

    with open(file_path, "a") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(fieldnames)
    csvFile.close()


# funciones para el funcionamiento de la partida
def velocidad_real(pil, v, pi):
    max(p.VELOCIDAD_MINIMA, velocidad_intencional(pil, v, pi)
        + dificultad_control(pil, v) + efecto_hipotermia(pi, pil))


def velocidad_recomendada(pil, v, pi):
    v_recomendada = (v.motor_zapatillas +
                     (v.ruedas - pi.hielo) * p.POND_EFECT_HIELO +
                     (v.carroceria - pi.rocas) * p.POND_EFECT_ROCAS +
                     (pil.experiencia - pil.dificultad) * p.POND_EFECT_DIFICULTAD)
    return v_recomendada


def velocidad_intencional(pil, v, pi):
    if pil.personalidad == "osado":
        velocidad = p.EFECTO_OSADO * velocidad_recomendada(pil, v, pi)
    else:
        velocidad = p.EFECTO_PRECAVIDO * velocidad_recomendada(pil, v, pi)
    return velocidad


def efecto_hipotermia(pi, pil):
    hipotermia = min(0, pi.numero_vueltas * (pil.contextura - pi.hielo))
    return hipotermia


def dificultad_control(pil, v):
    if v.categoria == "bicicleta" or v.categoria == "motocicleta":
        if pil.personalidad == "osado":
            dificultad = min(0, pil.equilibrio - p.PESO_MEDIO / v.peso)
            return dificultad
        else:
            dificultad = min(0, pil.equilibrio * p.EQUILIBRIO_PRECAVIDO - p.PESO_MEDIO / v.peso)
            return dificultad
    else:
        dificultad = 0
        return dificultad


def dano_vehiculo(v, pi):
    dano_recibido_cada_vuelta = max(0, pi.rocas - v.carroceria)
    return dano_recibido_cada_vuelta


def tiempo_pits(v):
    cat = v.categoria.upper()
    tiempo = (p.TIEMPO_MINIMO_PITS + (p.cat['CHASIS']['MIN']
                                      - v.chasis) * p.VELOCIDAD_PITS)
    return tiempo


def dinero_vuelta(pi):
    dinero = pi.numero_vueltas * pi.dificultad
    return dinero


def accidentes_vueltas(pil, v, pi):
    cat = v.categoria.upper()
    p_accidente = min(1, max(0, (velocidad_real(pil, v, pi)
                                 - velocidad_recomendada(pil, v, pi)
                                 ) / velocidad_recomendada(pil, v, pi)) +
                      (p.cat['CHASIS']['MAX'] - v.chasis) /
                      (p.cat['CHASIS']['MAX']))
    return p_accidente


def tiempo_vuelta(pil, v, pi):
    t_v = pi.largo / velocidad_real(pil, v, pi)
    return t_v


def dinero_por_ganar(pi):
    dinero_ganador = pi.numero_vueltas * (pi.dificultad + pi.hielo + pi.rocas)
    return dinero_ganador


def ventaja():
    pass


def experiencia_por_ganar():
    pass
