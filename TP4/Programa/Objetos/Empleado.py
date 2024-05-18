class Empleado:
    def __init__(self, numero, estado, minuto_salida_temporalmente, minuto_entrada_cola):
        self.numero = numero
        self.estado = estado
        self.minuto_salida_temporalmente = minuto_salida_temporalmente
        self.minuto_entrada_cola = minuto_entrada_cola

    def get_estado(self):
        return self.estado

    def get_minuto_salida_temporalmente(self):
        return self.minuto_salida_temporalmente

    def get_minuto_entrada_cola(self):
        return self.minuto_entrada_cola

    def set_estado(self, estado, terminal):
        self.estado = estado + terminal

    def set_minuto_salida_temporalmente(self, minuto):
        self.minuto_salida_temporalmente = minuto

    def set_minuto_entrada_cola(self, minuto):
        self.minuto_entrada_cola = minuto
