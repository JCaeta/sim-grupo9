class Empleado:
    def __init__(self, numero, estado, minuto_entrada_cola, terminal):
        self.numero = numero
        self.estado = estado
        self.minuto_entrada_cola = minuto_entrada_cola
        self.terminal = terminal

    def get_numero(self):
        return self.numero

    def get_estado(self):
        return self.estado

    def get_minuto_entrada_cola(self):
        return self.minuto_entrada_cola

    def get_terminal(self):
        return self.terminal
