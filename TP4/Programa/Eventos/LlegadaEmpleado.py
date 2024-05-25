class LlegadaEmpleado:
    def __init__(self, rnd, tiempo_entre_llegadas, proxima_llegada):
        self.nombre = "llegada_empleado"
        self.rnd = rnd
        self.tiempo_entre_llegadas = tiempo_entre_llegadas
        self.proxima_llegada = proxima_llegada

    def get_rnd(self):
        return self.rnd

    def get_tiempo_entre_llegadas(self):
        return self.tiempo_entre_llegadas

    def get_proxima_llegada(self):
        return self.get_proxima_llegada()