class Terminal:
    def __init__(self, numero, estado):
        self.numero = numero
        self.estado = estado

    def get_numero(self):
        return self.numero

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado
