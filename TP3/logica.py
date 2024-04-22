from generador_numeros import rnd

INGRESOS = 4000
COSTO = 2400
COSTO_OBRERO = 30
CANTIDAD_MINIMA_OBREROS_PRESENTES = 20

ausentismo = {
    0: 0.36,
    1: 0.74,
    2: 0.93,
    3: 0.99,
    4: 1,
}


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


def encontrar_ausentimo(rnd_obrero):
    for ausentes, probabilidad_acumulada in ausentismo.items():
        if rnd_obrero < probabilidad_acumulada:
            return ausentes

    return 4


def es_operable(cant_obreros):
    if (CANTIDAD_MINIMA_OBREROS_PRESENTES - cant_obreros) < 20:
        return "Si"
    return "No"


def simulacion(cant_dias, cant_obreros, rango_desde, rango_hasta):
    lista_simulacion = []
    beneficio_acumulado = 0

    for i in range(cant_dias):
        dia = i+1
        rnd_obrero = round(rnd(), 4)
        obreros_ausentes = encontrar_ausentimo(rnd_obrero)
        obreros_presentes = cant_obreros - obreros_ausentes
        planta_operable = es_operable(cant_obreros)
        ingresos_por_venta = 0
        costos_por_venta = 0

        if planta_operable:
            ingresos_por_venta = INGRESOS
            costos_por_venta = COSTO

        sueldos_obreros = cant_obreros * COSTO_OBRERO
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
        return lista_simulacion[rango_desde-1:rango_hasta]

    return lista_simulacion[rango_desde-1:rango_hasta] + [lista_simulacion[-1]]
