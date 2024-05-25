class Simulacion:
    def __init__(self):
        self.evento = ""
        self.proximo_evento = ""
        self.reloj = ""
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
        self.cola = ""
        self.rnd_fin_mantenimiento_terminal = ""
        self.tiempo_mantenimiento_terminal = ""
        self.fin_mantenimiento_terminal1 = ""
        self.fin_mantenimiento_terminal2 = ""
        self.fin_mantenimiento_terminal3 = ""
        self.fin_mantenimiento_terminal4 = ""
        self.acumulador_tiempo_espera = 0
        self.acumulador_empleados_que_salen_temporalmente = 0
        self.acumulador_empleados_que_pasaron_por_el_sistema = 0
        self.terminales = []
        self.estado_tecnico = "L"
        self.mantenimiento_t1 = ""
        self.mantenimiento_t2 = ""
        self.mantenimiento_t3 = ""
        self.mantenimiento_t4 = ""
        self.tecnico = []
        self.empleados = []


    def imprimir_columnas(self, iteracion):
        estado_terminales = self.get_estado_terminales()
        return (f'{'-'*10} Iteracion nº: {iteracion} {'-'*10}\nEvento: {self.get_evento()}\nProximo evento: '
                f'{self.get_proximo_evento()}\nReloj: {self.reloj}\nLlegadaEmpleado \n\tRND: {
                self.rnd_llegada_empleado}\n\tTiempo entre llegadas: {
                self.tiempo_entre_llegadas_empleado}\n\tProxima llegada empleado: {self.proxima_llegada_empleado}\n'
                f'LlegadaTecnico \n\tRND: {self.rnd_llegada_tecnico}\n\tTiempo en llegar: '
                f'{self.tiempo_en_llegar_tecnico}\n\tProxima llegada tecnico: {self.proxima_llegada_tecnico}\n'
                f'FinRegistroHuella \n\tRND: {self.rnd_fin_registro_huella}\n\tTiempo registro huella: '
                f'{self.tiempo_registro_huella}\n\tFin Registro Huella T1: {self.fin_registro_huella_t1}\n\t'
                f'Fin Registro Huella T2: {self.fin_registro_huella_t2}\n\t'
                f'Fin Registro Huella T3: {self.fin_registro_huella_t3}\n\tFin Registro Huella T4: '
                f'{self.fin_registro_huella_t4}\nFinMantenimientoTerminal\n\tRND: '
                f'{self.rnd_fin_mantenimiento_terminal}\n\tTiempo Mantenimiento Terminal: '
                f'{self.tiempo_mantenimiento_terminal}\n\tFin Mantenimiento T1: {self.fin_mantenimiento_terminal1}\n\t'
                f'Fin Mantenimiento T2: {self.fin_mantenimiento_terminal2}\n\tFin Mantenimiento T3: '
                f'{self.fin_mantenimiento_terminal3}\n\tFin Mantenimiento T4: {self.fin_mantenimiento_terminal4}\n'
                f'AC Tiempo Espera: {self.acumulador_tiempo_espera}\nAC Empleados que salen temporalmente: {
                self.acumulador_empleados_que_salen_temporalmente}\nAC Empleados que pasaron por el sistema: '
                f'{self.acumulador_empleados_que_pasaron_por_el_sistema}\nTerminales\n\tEstado T1: '
                f'{estado_terminales[0]}\n\tEstado T2: {estado_terminales[1]}\n\tEstado T3: {estado_terminales[2]}\n\t'
                f'Estado T4: {estado_terminales[3]}\n\tCola: {self.get_cola()}\nTecnico'
                f'{self.get_info_tecnico()}\n'
                f'Empleado{self.get_info_empleados()}\n{'-'*40}')

    def get_reloj(self):
        return self.reloj

    def get_evento(self):
        return self.evento

    def get_proximo_evento(self):
        return self.proximo_evento

    def get_cola(self):
        return self.cola

    def get_terminales_libres(self):
        terminales_libres = []
        for i in range(len(self.terminales)):
            if self.terminales[i].get_estado() == "L":
                terminales_libres.append(self.terminales[i].get_numero())

        return terminales_libres

    def get_terminales_disponibles(self):
        terminales_libres = self.get_terminales_libres()

        if len(terminales_libres) > 0:
            return terminales_libres

        terminales_disponibles = []
        for i in range(len(self.terminales)):
            if self.terminales[i].get_estado() == "OM":
                terminales_disponibles.append(self.terminales[i].get_numero())

        return terminales_disponibles

    def get_estado_terminales(self):
        estado_terminales = []
        for i in range(len(self.terminales)):
            estado_terminales.append(self.terminales[i].get_estado())

        return estado_terminales

    def get_info_empleados(self):
        info = ""
        for i in range(len(self.empleados)):
            info += (f'\n\tNº Empleado: {self.empleados[i].get_numero()}\n\t'
                     f'Estado: {self.empleados[i].get_estado()}\n\t'
                     f'Minuto que entra en cola: {self.empleados[i].get_minuto_entrada_cola()}\n\t')
        return info

    def buscar_empleado_cola(self):
        empleado = None
        menor_cola = 1000000000000000
        for i in range(len(self.empleados)):
            if self.empleados[i].get_minuto_entrada_cola() != "":
                minuto_entrada_cola = self.empleados[i].get_minuto_entrada_cola()
                if minuto_entrada_cola < menor_cola:
                    menor_cola = self.empleados[i].get_minuto_entrada_cola()
                    empleado = self.empleados[i]
            else:
                continue
        return empleado

    def buscar_indice_empleado(self, numero_empleado):
        for i in range(len(self.empleados)):
            if self.empleados[i].get_numero() == numero_empleado:
                return i

    def eliminar_empleado(self, numero_empleado):
        for i in range(len(self.empleados)):
            if self.empleados[i].get_numero() == numero_empleado:
                del self.empleados[i]
                break

    def buscar_empleado(self, numero_terminal):
        for i in range(len(self.empleados)):
            if self.empleados[i].get_terminal() == numero_terminal:
                return self.empleados[i]

    def get_info_tecnico(self):
        info = ""
        info += (f'\n\tEstado: {self.estado_tecnico}\n\t'
                 f'Mantenimiento T1: {self.mantenimiento_t1}\n\t'
                 f'Mantenimiento T2: {self.mantenimiento_t2}\n\t'
                 f'Mantenimiento T3: {self.mantenimiento_t3}\n\t'
                 f'Mantenimiento T4: {self.mantenimiento_t4}')

        return info

    def encontrar_terminales_restantes_a_mantener(self, terminal_arreglada):
        terminales_restantes_a_mantener = []

        if self.mantenimiento_t1 == "NO" and self.terminales[0].get_numero != terminal_arreglada:
            terminales_restantes_a_mantener.append(1)

        if self.mantenimiento_t2 == "NO" and self.terminales[0].get_numero != terminal_arreglada:
            terminales_restantes_a_mantener.append(2)

        if self.mantenimiento_t3 == "NO" and self.terminales[0].get_numero != terminal_arreglada:
            terminales_restantes_a_mantener.append(3)

        if self.mantenimiento_t4 == "NO" and self.terminales[0].get_numero != terminal_arreglada:
            terminales_restantes_a_mantener.append(4)

        return terminales_restantes_a_mantener


