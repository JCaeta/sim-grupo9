from generador_numeros import rnd


class Parametros:
    def __init__(self, ingresos_venta, costo_venta, remuneracion_obrero):
        self.ingresos_venta = ingresos_venta
        self.costo_venta = costo_venta
        self.remuneracion_obrero = remuneracion_obrero
        self.probabilidades = []

    def getIngreso(self):
        return self.ingresos_venta

    def getCostoVenta(self):
        return self.costo_venta

    def getRemuneracionObrero(self):
        return self.remuneracion_obrero

    def setIngreso(self, ingreso):
        self.ingresos_venta = ingreso

    def setCostoVenta(self, costo):
        self.costo_venta = costo

    def setRemuneracionObrero(self, remuneracion):
        self.remuneracion_obrero = remuneracion

    def setear_probabilidades(self, frecuencias):
        frecuencias_acumuladas = sum(frecuencias)
        probabilidad_acumulada = 0

        for ausentes, frecuencia in enumerate(frecuencias):
            probabilidad = round((frecuencia / frecuencias_acumuladas), 4)
            probabilidad_acumulada += probabilidad
            self.probabilidades.append((ausentes, probabilidad_acumulada))

    def getProbabilidad(self):
        return self.probabilidades


class Simulacion:
    def __init__(self, dia, rnd_obrero, obreros_ausentes, obreros_presentes, planta_operable, beneficio,
                 beneficio_acumulado):
        self.dia = dia
        self.rnd_obrero = rnd_obrero
        self.obreros_ausentes = obreros_ausentes
        self.obreros_presentes = obreros_presentes
        self.planta_operable = planta_operable
        self.beneficio = beneficio
        self.beneficio_acumulado = beneficio_acumulado

    def get_dia(self):
        return self.dia

    def set_dia(self, dia):
        self.dia = dia

    def get_rnd_obrero(self):
        return self.rnd_obrero

    def set_rnd_obrero(self, rnd_obrero):
        self.rnd_obrero = rnd_obrero

    def get_obreros_ausentes(self):
        return self.obreros_ausentes

    def set_obreros_ausentes(self, obreros_ausentes):
        self.obreros_ausentes = obreros_ausentes

    def get_obreros_presentes(self):
        return self.obreros_presentes

    def set_obreros_presentes(self, obreros_presentes):
        self.obreros_presentes = obreros_presentes

    def get_planta_operable(self):
        return self.planta_operable

    def set_planta_operable(self, booleano):
        self.planta_operable = booleano

    def get_beneficio(self):
        return self.beneficio

    def set_beneficio(self, beneficio):
        self.beneficio = beneficio

    def get_beneficio_acumulado(self):
        return self.beneficio_acumulado

    def set_beneficio_acumulado(self, beneficio_acumulado):
        self.beneficio_acumulado = beneficio_acumulado


def encontrar_ausentismo(rnd_obrero, objeto_parametros):
    probabilidades = objeto_parametros.getProbabilidad()

    for ausentes, probabilidad_acumulada in probabilidades:
        if rnd_obrero < probabilidad_acumulada:
            return ausentes
        
    return probabilidades[-1][0]

def es_operable(obreros_presentes):
    if obreros_presentes >= 20:
        return "Si"
    return "No"


def simulacion(cant_dias, cant_obreros, rango_desde, rango_hasta, objeto_parametros):
    lista_simulacion = []
    beneficio_acumulado = 0

    for i in range(cant_dias):
        dia = i + 1
        rnd_obrero = round(rnd(), 4)

        obreros_ausentes = encontrar_ausentismo(rnd_obrero, objeto_parametros)
        obreros_presentes = cant_obreros - obreros_ausentes

        planta_operable = es_operable(obreros_presentes)

        ingresos_por_venta = 0
        costos_por_venta = 0

        if planta_operable == "Si":
            ingresos_por_venta = objeto_parametros.getIngreso()
            costos_por_venta = objeto_parametros.getCostoVenta()

        sueldos_obreros = cant_obreros * objeto_parametros.getRemuneracionObrero()

        beneficio = ingresos_por_venta - costos_por_venta - sueldos_obreros
        beneficio_acumulado += beneficio

        sim = Simulacion(
            dia=dia,
            rnd_obrero=rnd_obrero,
            obreros_ausentes=obreros_ausentes,
            obreros_presentes=obreros_presentes,
            planta_operable=planta_operable,
            beneficio=beneficio,
            beneficio_acumulado=beneficio_acumulado
        )

        lista_simulacion.append(sim)

    ultimo_dia = lista_simulacion[-1].dia

    if len(lista_simulacion) == 1:
        return lista_simulacion

    if rango_hasta == ultimo_dia:
        return lista_simulacion[rango_desde - 1:rango_hasta]

    return lista_simulacion[rango_desde - 1:rango_hasta] + [lista_simulacion[-1]]
