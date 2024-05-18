class EventosYAuxiliares:
    def __init__(self, evento, reloj, proximo_evento):
        self.evento = evento
        self.proximo_evento = proximo_evento
        self.reloj = reloj
        self.rnd_llegada_empleado = ""
        self.tiempo_entre_llegadas_empleado = ""
        self.proxima_llegada_empleado = ""
        self.rnd_llegada_tecnico = ""
        self.tiempo_en_llegar_tecnico = ""
        self.proxima_llegada_tecnico = ""
        self.rnd_fin_registro_huella = ""
        self.tiempo_registro_huella = ""
        self.fin_registro_huella_t1 = ""
        self.fin_registro_huella_t2 = ""
        self.fin_registro_huella_t3 = ""
        self.fin_registro_huella_t4 = ""
        self.rnd_fin_mantenimiento_terminal = ""
        self.tiempo_mantenimiento_terminal = ""
        self.fin_mantenimiento_t1 = ""
        self.fin_mantenimiento_t2 = ""
        self.fin_mantenimiento_t3 = ""
        self.fin_mantenimiento_t4 = ""
        self.acumulador_tiempo_espera = ""
        self.contador_empleados_que_salen_temporalmente = ""
        self.estado_tecnico = ""
        self.empleados = []
