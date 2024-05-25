import random
import math


class Simulacion:
    def __init__(self):
        self.evento = "Inicialización"
        self.proximo_evento = ""
        self.reloj = 0.0
        self.rnd_llegada_empleado = None
        self.tiempo_entre_llegadas_empleado = None
        self.proxima_llegada_empleado = None
        self.rnd_llegada_tecnico = None
        self.tiempo_entre_llegadas_tecnico = None
        self.proxima_llegada_tecnico = None
        self.rnd_registro_huella = None
        self.tiempo_registro_huella = None
        self.fin_registro_huella = [None, None, None, None]
        self.cola = 0
        self.rnd_mantenimiento_terminal = None
        self.tiempo_mantenimiento_terminal = None
        self.fin_mantenimiento_terminal = [None, None, None, None]
        self.tecnico = Tecnico()
        self.terminales = [Terminal(i) for i in range(1, 5)]
        self.empleados = []
        self.acumulador_tiempo_espera = 0
        self.acumulador_empleados_que_salen_temporalmente = 0
        self.acumulador_empleados_que_pasaron_por_el_sistema = 0
        self.tiempo_maximo = 480  # 8 horas, por ejemplo
        self.numero_empleado = 1

