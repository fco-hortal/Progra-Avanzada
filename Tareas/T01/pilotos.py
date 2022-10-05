import parametros as p


class Piloto:
    def __init__(self, juego):
        self.juego = juego
        self.nombre = None
        self.personalidad = None
        self.contextura = None
        self.equilibrio = None
        self.experiencia = 0
        self.dinero = 0
        self.equipo = None

    def rellenar_piloto_inicio(self):
        if self.equipo == "Tareos":
            self.contextura = p.EQUIPOS['TAREOS']['CONTEXTURA']['MIN']
            self.equilibrio = p.EQUIPOS['TAREOS']['EQUILIBRIO']['MIN']
            self.personalidad = p.EQUIPOS['TAREOS']['PERSONALIDAD']
        elif self.equipo == "Hibridos":
            self.contextura = p.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MIN']
            self.equilibrio = p.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MIN']
            self.personalidad = p.EQUIPOS['HIBRIDOS']['PERSONALIDAD']
        elif self.equipo == "Docencios":
            self.contextura = p.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MIN']
            self.equilibrio = p.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MIN']
            self.personalidad = p.EQUIPOS['DOCENCIOS']['PERSONALIDAD']
