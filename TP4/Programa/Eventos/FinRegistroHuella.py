class FinRegistroHuella:
    def __init__(self, rnd, tiempo_registro_huella, fin_t1, fin_t2, fin_t3, fin_t4):
        self.nombre = "fin_registro_huella"
        self.rnd = rnd
        self.tiempo_registro_huella = tiempo_registro_huella
        self.fin_registro_huella_t1 = fin_t1
        self.fin_registro_huella_t2 = fin_t2
        self.fin_registro_huella_t3 = fin_t3
        self.fin_registro_huella_t4 = fin_t4


    def get_rnd(self):
        return self.rnd

    def get_tiempo_entre_llegadas(self):
        return self.tiempo_registro_huella

    def get_fin_registro_huella_t1(self):
        return self.fin_registro_huella_t1

    def get_fin_registro_huella_t2(self):
        return self.fin_registro_huella_t2

    def get_fin_registro_huella_t3(self):
        return self.fin_registro_huella_t3

    def get_fin_registro_huella_t4(self):
        return self.fin_registro_huella_t4
