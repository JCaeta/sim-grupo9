class FinMantenimientoTerminal:
    def __init__(self, rnd, tiempo_mantenimiento_terminal, mantenimiento_t1, mantenimiento_t2, mantenimiento_t3, mantenimiento_t4):
        self.nombre = "fin_mantenimiento_terminal"
        self.rnd = rnd
        self.tiempo_mantenimiento_terminal = tiempo_mantenimiento_terminal
        self.fin_mantenimiento_t1 = mantenimiento_t1
        self.fin_mantenimiento_t2 = mantenimiento_t2
        self.fin_mantenimiento_t3 = mantenimiento_t3
        self.fin_mantenimiento_t4 = mantenimiento_t4

    def get_rnd(self):
        return self.rnd

    def get_tiempo_entre_llegadas(self):
        return self.tiempo_mantenimiento_terminal

    def get_fin_mantenimiento_t1(self):
        return self.fin_mantenimiento_t1

    def get_fin_mantenimiento_t2(self):
        return self.fin_mantenimiento_t2

    def get_fin_mantenimiento_t3(self):
        return self.fin_mantenimiento_t3

    def get_fin_mantenimiento_t4(self):
        return self.fin_mantenimiento_t4
