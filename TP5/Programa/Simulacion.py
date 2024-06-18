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
        self.rnd_cant_archivos = ""
        self.cant_archivos = ""
        self.tiempo_mantenimiento_terminal = ""
        self.fin_mantenimiento_terminal1 = ""
        self.fin_mantenimiento_terminal2 = ""
        self.fin_mantenimiento_terminal3 = ""
        self.fin_mantenimiento_terminal4 = ""
        self.acumulador_tiempo_espera = 0
        self.acumulador_empleados_que_salen_temporalmente = 0
        self.acumulador_empleados_que_pasaron_por_el_sistema = 0
        self.lista_estado_terminales = []
        self.terminales = []
        self.estado_tecnico = "L"
        self.mantenimiento_t1 = ""
        self.mantenimiento_t2 = ""
        self.mantenimiento_t3 = ""
        self.mantenimiento_t4 = ""
        self.tecnico = []
        self.lista_empleados = []
        self.empleados = []

    def imprimir_columnas(self, iteracion):
        estado_terminales = self.get_estado_terminales()
        return (
            f"{'-'*10} Iteracion nº: {iteracion} {'-'*10}\n"
            f"Evento: {self.get_evento()}\n"
            f"Proximo evento: {self.get_proximo_evento()}\n"
            f"Reloj: {self.reloj}\n"
            f"LlegadaEmpleado \n\tRND: {self.rnd_llegada_empleado}\n\tTiempo entre llegadas: {self.tiempo_entre_llegadas_empleado}\n\tProxima llegada empleado: {self.proxima_llegada_empleado}\n"
            f"LlegadaTecnico \n\tRND: {self.rnd_llegada_tecnico}\n\tTiempo en llegar: {self.tiempo_en_llegar_tecnico}\n\tProxima llegada tecnico: {self.proxima_llegada_tecnico}\n"
            f"FinRegistroHuella \n\tRND: {self.rnd_fin_registro_huella}\n\tTiempo registro huella: {self.tiempo_registro_huella}\n\tFin Registro Huella T1: {self.fin_registro_huella_t1}\n\t"
            f"Fin Registro Huella T2: {self.fin_registro_huella_t2}\n\t"
            f"Fin Registro Huella T3: {self.fin_registro_huella_t3}\n\tFin Registro Huella T4: {self.fin_registro_huella_t4}\n"
            f"FinMantenimientoTerminal\n\tRND: {self.rnd_fin_mantenimiento_terminal}\n\tTiempo Mantenimiento Terminal: {self.tiempo_mantenimiento_terminal}\n\tFin Mantenimiento T1: {self.fin_mantenimiento_terminal1}\n\t"
            f"Fin Mantenimiento T2: {self.fin_mantenimiento_terminal2}\n\tFin Mantenimiento T3: {self.fin_mantenimiento_terminal3}\n\tFin Mantenimiento T4: {self.fin_mantenimiento_terminal4}\n"
            f"AC Tiempo Espera: {self.acumulador_tiempo_espera}\n"
            f"AC Empleados que salen temporalmente: {self.acumulador_empleados_que_salen_temporalmente}\n"
            f"AC Empleados que pasaron por el sistema: {self.acumulador_empleados_que_pasaron_por_el_sistema}\n"
            f"Terminales\n\tEstado T1: {estado_terminales[0]}\n\tEstado T2: {estado_terminales[1]}\n\tEstado T3: {estado_terminales[2]}\n\tEstado T4: {estado_terminales[3]}\n\tCola: {self.get_cola()}\n"
            f"Tecnico{self.get_info_tecnico()}\nEmpleados\n{self.get_info_empleados()}"
        )
        
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

    def get_estado_terminales(self):
        estado_terminales = []
        for i in range(len(self.terminales)):
            estado_terminales.append(self.terminales[i].get_estado())

        return estado_terminales

    def get_info_empleados(self):
        info = ""
        for i in self.empleados:
            info += f'\tEmpleado nº {i.get_numero()} - Estado: {i.get_estado()} - Min. EC: {i.get_minuto_entrada_cola()} - Terminal: {i.get_terminal()}\n'

        return info

    def get_info_terminales(self):
        info_terminales = []
        for i in self.lista_estado_terminales:
            for j in range(4):
                info = {
                    f'Estado T{j+1}': i[j]
                }

                info_terminales.append(info)

        return info_terminales

    def actualizar_info_empleados(self):
        for i in self.empleados:
            estado_empleado = i.get_estado()
            minuto_entrada = i.get_minuto_entrada_cola()

            self.lista_empleados.append([estado_empleado, minuto_entrada],)

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
                self.empleados[i].numero = ""
                self.empleados[i].estado = ""
                self.empleados[i].minuto_entrada_cola = ""
                self.empleados[i].terminal = ""
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

    def get_terminal_a_mantener(self, terminal_arreglada):
        terminales_restantes_a_mantener = []

        if self.mantenimiento_t1 == "NO" and terminal_arreglada != 1:
            terminales_restantes_a_mantener.append(1)

        if self.mantenimiento_t2 == "NO" and terminal_arreglada != 2:
            terminales_restantes_a_mantener.append(2)

        if self.mantenimiento_t3 == "NO" and terminal_arreglada != 3:
            terminales_restantes_a_mantener.append(3)

        if self.mantenimiento_t4 == "NO" and terminal_arreglada != 4:
            terminales_restantes_a_mantener.append(4)

        # Si hay terminales por mantener, nos fijamos ahora si están libres
        if len(terminales_restantes_a_mantener) > 0:
            terminales_candidatas = []
            for i in self.terminales:
                if i.get_estado() == "L" and i.get_numero() in terminales_restantes_a_mantener:
                    terminales_candidatas.append(i.get_numero())

            # Si tenemos 1 o más terminales candidatas, elegimos la primera
            if len(terminales_candidatas) > 0:
                return terminales_candidatas[0]

            # Si encontramos que falta mantenimiento, pero están ocupadas, significa que el tecnico tiene que esperar a que se libere
            return False

        # Si no hay mas terminales por mantener
        return -1

    def to_dict(self):
        estado_terminales = self.get_info_terminales()

        simulaciones_dict = {
            'Evento': self.evento,
            'Proximo Evento': self.proximo_evento,
            'Reloj': self.reloj,
            'RND Llegada Empleado': self.rnd_llegada_empleado,
            'Tiempo entre Llegadas Empleado': self.tiempo_entre_llegadas_empleado,
            'Proxima Llegada Empleado': self.proxima_llegada_empleado,
            'RND Llegada Tecnico': self.rnd_llegada_tecnico,
            'Tiempo en Llegar Tecnico': self.tiempo_en_llegar_tecnico,
            'Proxima Llegada Tecnico': self.proxima_llegada_tecnico,
            'RND Fin Registro Huella': self.rnd_fin_registro_huella,
            'Tiempo Registro Huella': self.tiempo_registro_huella,
            'Fin Registro Huella T1': self.fin_registro_huella_t1,
            'Fin Registro Huella T2': self.fin_registro_huella_t2,
            'Fin Registro Huella T3': self.fin_registro_huella_t3,
            'Fin Registro Huella T4': self.fin_registro_huella_t4,
            'Estado T1': estado_terminales[0]['Estado T1'],
            'Estado T2': estado_terminales[1]['Estado T2'],
            'Estado T3': estado_terminales[2]['Estado T3'],
            'Estado T4': estado_terminales[3]['Estado T4'],
            'Cola': self.cola,
            'RND Cant Archivos': self.rnd_cant_archivos,
            'Cant Archivos': self.cant_archivos,
            'Tiempo Mantenimiento Terminal': self.tiempo_mantenimiento_terminal,
            'Fin Mantenimiento T1': self.fin_mantenimiento_terminal1,
            'Fin Mantenimiento T2': self.fin_mantenimiento_terminal2,
            'Fin Mantenimiento T3': self.fin_mantenimiento_terminal3,
            'Fin Mantenimiento T4': self.fin_mantenimiento_terminal4,
            'AC Tiempo Espera': self.acumulador_tiempo_espera,
            'AC Empleados que Salen Temporalmente': self.acumulador_empleados_que_salen_temporalmente,
            'AC Empleados que Pasaron por el Sistema': self.acumulador_empleados_que_pasaron_por_el_sistema,
            'Estado Tecnico': self.estado_tecnico,
            'Mantenimiento T1': self.mantenimiento_t1,
            'Mantenimiento T2': self.mantenimiento_t2,
            'Mantenimiento T3': self.mantenimiento_t3,
            'Mantenimiento T4': self.mantenimiento_t4,
        }

        for i in range(len(self.lista_empleados)):
            columna_estado = f'Estado Emp. {i+1}'
            columna_min_cola = f'Min. entrada cola Emp. {i+1}'

            dato_estado = self.lista_empleados[i][0]
            dato_min_cola = self.lista_empleados[i][1]

            simulaciones_dict[columna_estado] = dato_estado
            simulaciones_dict[columna_min_cola] = dato_min_cola
        
        return simulaciones_dict
