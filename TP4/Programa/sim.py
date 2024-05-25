import random

from Distribuciones import (DistribucionLlegadaTecnico, DistribucionLlegadaEmpleado, DistribucionFinRegistroHuella,
                            DistribucionFinMantenimientoTerminal)
from Objetos import Empleado
from Objetos import Terminal
from Simulacion import Simulacion
from utilidades import *


def simulacion(minutoARegistroHuella, minutoBRegistroHuella,
               minutoALlegadaTecnico, minutoBLlegadaTecnico,
               minutoAMantenimientoTerminal, minutoBMantenimientoTerminal,
               mediaLlegadaEmpleado, iteraciones, cantidad_datos_a_mostrar):

    # Inicialización de cada distribución

    dist_registro_huella = DistribucionFinRegistroHuella.DistribucionFinRegistroHuella(a=minutoARegistroHuella,
                                                                                       b=minutoBRegistroHuella)

    dist_tecnico = DistribucionLlegadaTecnico.DistribucionLlegadaTecnico(a=minutoALlegadaTecnico * 60 -
                                                                           minutoBLlegadaTecnico,
                                                                         b=minutoALlegadaTecnico * 60 +
                                                                           minutoBLlegadaTecnico)

    dist_mantenimiento_terminal = (DistribucionFinMantenimientoTerminal.
                                   DistribucionFinMantenimientoTerminal(a=minutoAMantenimientoTerminal,
                                                                        b=minutoBMantenimientoTerminal))

    dist_llegada_empleado = DistribucionLlegadaEmpleado.DistribucionLlegadaEmpleado(media=mediaLlegadaEmpleado)

    ############################################################

    simulaciones = []

    # Inicialización de la primera simulación

    evento = "Inicialización"
    reloj = 0.00

    rnd_llegada_empleado = round(rnd(), 2)
    tiempo_entre_llegadas_empleado = generador_exponencial(media=dist_llegada_empleado.get_media(),
                                                           random=rnd_llegada_empleado)
    proxima_llegada_empleado = round(reloj + tiempo_entre_llegadas_empleado, 2)

    rnd_llegada_tecnico = round(rnd(), 2)
    tiempo_entre_llegadas_tecnico = generador_uniforme(a=dist_tecnico.get_a(),
                                                       b=dist_tecnico.get_b(),
                                                       random=rnd_llegada_tecnico)
    proxima_llegada_tecnico = round(reloj + tiempo_entre_llegadas_tecnico, 2)

    terminales = [Terminal.Terminal(numero=i + 1)
                  for i in range(4)]

    fin_registro_huella_t1 = "-"
    fin_registro_huella_t2 = "-"
    fin_registro_huella_t3 = "-"
    fin_registro_huella_t4 = "-"

    fin_mantenimiento_t1 = "-"
    fin_mantenimiento_t2 = "-"
    fin_mantenimiento_t3 = "-"
    fin_mantenimiento_t4 = "-"

    cola_terminales = 0

    acumulador_tiempo_espera = 0
    acumulador_empleados_que_salen_temporalmente = 0
    acumulador_empleados_que_pasan_por_sistema = 0

    numero_empleado = 1
    empleados = []

    sim = Simulacion()

    sim.rnd_llegada_empleado = rnd_llegada_empleado
    sim.tiempo_entre_llegadas_empleado = tiempo_entre_llegadas_empleado
    sim.proxima_llegada_empleado = proxima_llegada_empleado

    sim.rnd_llegada_tecnico = rnd_llegada_tecnico
    sim.tiempo_en_llegar_tecnico = tiempo_entre_llegadas_tecnico
    sim.proxima_llegada_tecnico = proxima_llegada_tecnico

    sim.acumulador_tiempo_espera = acumulador_tiempo_espera
    sim.acumulador_empleados_que_salen_temporalmente = acumulador_empleados_que_salen_temporalmente
    sim.acumulador_empleados_que_pasaron_por_el_sistema = acumulador_empleados_que_pasan_por_sistema

    sim.evento = evento
    sim.cola = cola_terminales
    sim.reloj = reloj
    sim.terminales = terminales
    sim.empleados = empleados

    tiempos = {
        'llegada_empleado': proxima_llegada_empleado if proxima_llegada_empleado != '-' else float('inf'),
        'llegada_tecnico': proxima_llegada_tecnico if proxima_llegada_tecnico != '-' else float('inf'),
        'fin_registro_huella_t1': fin_registro_huella_t1 if fin_registro_huella_t1 != '-' else float('inf'),
        'fin_registro_huella_t2': fin_registro_huella_t2 if fin_registro_huella_t2 != '-' else float('inf'),
        'fin_registro_huella_t3': fin_registro_huella_t3 if fin_registro_huella_t3 != '-' else float('inf'),
        'fin_registro_huella_t4': fin_registro_huella_t4 if fin_registro_huella_t4 != '-' else float('inf'),
        'fin_mantenimiento_t1': fin_mantenimiento_t1 if fin_mantenimiento_t1 != '-' else float('inf'),
        'fin_mantenimiento_t2': fin_mantenimiento_t2 if fin_mantenimiento_t2 != '-' else float('inf'),
        'fin_mantenimiento_t3': fin_mantenimiento_t3 if fin_mantenimiento_t3 != '-' else float('inf'),
        'fin_mantenimiento_t4': fin_mantenimiento_t4 if fin_mantenimiento_t4 != '-' else float('inf'),
    }

    menor_tiempo_key = min(tiempos, key=tiempos.get)
    menor_tiempo = tiempos[menor_tiempo_key]
    proximo_evento = menor_tiempo_key

    if proximo_evento.startswith("llegada_empleado"):
        proximo_evento += '(' + str(numero_empleado) + ')'

    sim.proximo_evento = proximo_evento
    simulaciones.append(sim)

    print(simulaciones[0].imprimir_columnas(0))

    for i in range(1, 70):
        simulaciones.append(Simulacion())
        reloj = menor_tiempo
        evento = simulaciones[i - 1].proximo_evento
        simulaciones[i].evento = evento
        simulaciones[i].reloj = reloj
        simulaciones[i].empleados = simulaciones[i - 1].empleados

        simulaciones[i].terminales = simulaciones[i - 1].terminales

        # Si llega un empleado
        if evento.startswith("llegada_empleado"):
            # y la cola todavía no es del máximo aceptado por el mismo
            if simulaciones[i - 1].get_cola() <= 5:
                terminales_libres = simulaciones[i - 1].get_terminales_disponibles()

                # Si hay terminales libres, elige una al azar
                if len(terminales_libres) > 0:
                    numero_terminal_elegida = random.choice(terminales_libres)
                    empleado = Empleado.Empleado(numero=numero_empleado,
                                                 estado="HR" + '(' + str(numero_terminal_elegida) + ')',
                                                 minuto_entrada_cola="",
                                                 terminal=numero_terminal_elegida)

                    simulaciones[i].terminales[numero_terminal_elegida - 1].estado = "OR"
                    rnd_registro_huella = round(rnd(), 2)
                    tiempo_registro_huella = generador_uniforme(a=dist_registro_huella.get_a(),
                                                                b=dist_registro_huella.get_b(),
                                                                random=rnd_registro_huella)
                    simulaciones[i].rnd_fin_registro_huella = rnd_registro_huella
                    simulaciones[i].tiempo_registro_huella = tiempo_registro_huella

                    if numero_terminal_elegida == 1:
                        simulaciones[i].fin_registro_huella_t1 = round(reloj + tiempo_registro_huella, 2)
                        simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                        simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                        simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                    if numero_terminal_elegida == 2:
                        simulaciones[i].fin_registro_huella_t2 = round(reloj + tiempo_registro_huella, 2)
                        simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                        simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                        simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                    if numero_terminal_elegida == 3:
                        simulaciones[i].fin_registro_huella_t3 = round(reloj + tiempo_registro_huella, 2)
                        simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                        simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                        simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                    if numero_terminal_elegida == 4:
                        simulaciones[i].fin_registro_huella_t4 = round(reloj + tiempo_registro_huella, 2)
                        simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                        simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                        simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1

                # Si todas las terminales están ocupadas, el empleado se va a la cola
                else:
                        empleado = Empleado.Empleado(numero=numero_empleado,
                                                     estado="EC",
                                                     minuto_entrada_cola=reloj,
                                                     terminal="")

                        cola_terminales += 1
                        simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                        simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                        simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                        simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                rnd_llegada_empleado = round(rnd(), 2)
                tiempo_entre_llegadas_empleado = generador_exponencial(media=dist_llegada_empleado.get_media(),
                                                                       random=rnd_llegada_empleado)
                proxima_llegada_empleado = round(reloj + tiempo_entre_llegadas_empleado, 2)

                simulaciones[i].rnd_llegada_empleado = rnd_llegada_empleado
                simulaciones[i].tiempo_entre_llegadas_empleado = tiempo_entre_llegadas_empleado
                simulaciones[i].empleados.append(empleado)

            # Caso en el que el cliente regresa a la media hora
            else:
                proxima_llegada_empleado = round(reloj + 30, 2)
                simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

            simulaciones[i].cola = cola_terminales
            simulaciones[i].fin_mantenimiento_terminal1 = simulaciones[i-1].fin_mantenimiento_terminal1
            simulaciones[i].fin_mantenimiento_terminal2 = simulaciones[i-1].fin_mantenimiento_terminal2
            simulaciones[i].fin_mantenimiento_terminal3 = simulaciones[i-1].fin_mantenimiento_terminal3
            simulaciones[i].fin_mantenimiento_terminal4 = simulaciones[i-1].fin_mantenimiento_terminal4
            simulaciones[i].mantenimiento_t1 = simulaciones[i-1].mantenimiento_t1
            simulaciones[i].mantenimiento_t2 = simulaciones[i-1].mantenimiento_t2
            simulaciones[i].mantenimiento_t3 = simulaciones[i-1].mantenimiento_t3
            simulaciones[i].mantenimiento_t4 = simulaciones[i-1].mantenimiento_t4
            simulaciones[i].proxima_llegada_empleado = proxima_llegada_empleado
            numero_empleado += 1
            simulaciones[i].proxima_llegada_tecnico = simulaciones[i - 1].proxima_llegada_tecnico
            simulaciones[i].estado_tecnico = simulaciones[i - 1].estado_tecnico
            simulaciones[i].acumulador_tiempo_espera = simulaciones[i - 1].acumulador_tiempo_espera
            simulaciones[i].acumulador_empleados_que_salen_temporalmente = simulaciones[
                i - 1].acumulador_empleados_que_salen_temporalmente
            simulaciones[i].acumulador_empleados_que_pasaron_por_el_sistema = simulaciones[
                i - 1].acumulador_empleados_que_pasaron_por_el_sistema

        # Si llega el técnico
        elif evento.startswith("llegada_tecnico"):
            terminales_libres = simulaciones[i - 1].get_terminales_libres()

            # Si hay terminales libres, elige la primera
            if len(terminales_libres) > 0:
                numero_terminal_elegida = terminales_libres[0]

            # Si no hay terminales libres, elige al azar
            else:
                numero_terminal_elegida = random.choice(simulaciones[i - 1].terminales)
                numero_terminal_elegida = numero_terminal_elegida.get_numero()

            simulaciones[i].rnd_fin_mantenimiento_terminal = round(rnd(), 2)
            simulaciones[i].tiempo_mantenimiento_terminal = generador_uniforme(
                a=dist_mantenimiento_terminal.get_a(),
                b=dist_mantenimiento_terminal.get_b(),
                random=simulaciones[i].rnd_fin_mantenimiento_terminal)

            simulaciones[i].estado_tecnico = "RM" + "(" + str(numero_terminal_elegida) + ")"

            if numero_terminal_elegida == 1:
                simulaciones[i].fin_mantenimiento_terminal1 = round(simulaciones[i].tiempo_mantenimiento_terminal
                                                             + simulaciones[i].reloj, 2)
            if numero_terminal_elegida == 2:
                simulaciones[i].fin_mantenimiento_terminal2 = round(simulaciones[i].tiempo_mantenimiento_terminal
                                                             + simulaciones[i].reloj, 2)
            if numero_terminal_elegida == 3:
                simulaciones[i].fin_mantenimiento_terminal3 = round(simulaciones[i].tiempo_mantenimiento_terminal
                                                             + simulaciones[i].reloj, 2)
            if numero_terminal_elegida == 4:
                simulaciones[i].fin_mantenimiento_terminal4 = round(simulaciones[i].tiempo_mantenimiento_terminal
                                                             + simulaciones[i].reloj, 2)

            if simulaciones[i - 1].terminales[numero_terminal_elegida - 1].get_estado() == "OR":
                simulaciones[i].terminales[numero_terminal_elegida - 1].estado = "ORM"

            elif simulaciones[i - 1].terminales[numero_terminal_elegida - 1].get_estado() == "L":
                simulaciones[i].terminales[numero_terminal_elegida - 1].estado = "OM"

            simulaciones[i].mantenimiento_t1 = "NO"
            simulaciones[i].mantenimiento_t2 = "NO"
            simulaciones[i].mantenimiento_t3 = "NO"
            simulaciones[i].mantenimiento_t4 = "NO"
            simulaciones[i].proxima_llegada_empleado = simulaciones[i - 1].proxima_llegada_empleado
            simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
            simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
            simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
            simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4
            simulaciones[i].cola = simulaciones[i - 1].cola
            simulaciones[i].acumulador_tiempo_espera = simulaciones[i - 1].acumulador_tiempo_espera
            simulaciones[i].acumulador_empleados_que_pasaron_por_el_sistema = simulaciones[
                i - 1].acumulador_empleados_que_pasaron_por_el_sistema
            simulaciones[i].acumulador_empleados_que_salen_temporalmente = simulaciones[
                i - 1].acumulador_empleados_que_salen_temporalmente

        # Si se termina de registrar una huella en una terminal
        elif evento.startswith("fin_registro_huella"):
            numero_terminal_fin = evento[-2]

            # Si tenemos algun empleado en cola esperando
            if simulaciones[i - 1].get_cola() > 0:
                # Encontrar el siguiente empleado en cola
                siguiente_empleado = simulaciones[i].buscar_empleado_cola()
                num_empleado = siguiente_empleado.get_numero()
                indice_empleado = simulaciones[i].buscar_indice_empleado(num_empleado)

                # Cambiar el estado de ese empleado de EC a HR
                estado_empleado = "HR" + '(' + numero_terminal_fin + ')'

                cola_terminales -= 1
                simulaciones[i].cola = cola_terminales

                simulaciones[i].rnd_fin_registro_huella = round(rnd(), 2)
                simulaciones[i].tiempo_registro_huella = generador_uniforme(a=dist_registro_huella.get_a(),
                                                                            b=dist_registro_huella.get_b(),
                                                                            random=simulaciones[
                                                                                i].rnd_fin_registro_huella)

                simulaciones[i].acumulador_tiempo_espera = round(simulaciones[i - 1].acumulador_tiempo_espera +
                                                                 simulaciones[i].reloj -
                                                                 simulaciones[i].empleados[
                                                                     indice_empleado].get_minuto_entrada_cola(), 2)

                simulaciones[i].empleados[indice_empleado].estado = estado_empleado
                simulaciones[i].empleados[indice_empleado].minuto_entrada_cola = ""
                simulaciones[i].empleados[indice_empleado].terminal = int(numero_terminal_fin)

                simulaciones[i].terminales[int(numero_terminal_fin) - 1].estado = simulaciones[i - 1].terminales[
                    int(numero_terminal_fin) - 1].estado

                if numero_terminal_fin == "1":
                    simulaciones[i].fin_registro_huella_t1 = round(reloj + simulaciones[i].tiempo_registro_huella, 2)
                    simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                    simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                    simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                elif numero_terminal_fin == "2":
                    simulaciones[i].fin_registro_huella_t2 = round(reloj + simulaciones[i].tiempo_registro_huella, 2)
                    simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                    simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                    simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                elif numero_terminal_fin == "3":
                    simulaciones[i].fin_registro_huella_t3 = round(reloj + simulaciones[i].tiempo_registro_huella, 2)
                    simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                    simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                    simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                elif numero_terminal_fin == "4":
                    simulaciones[i].fin_registro_huella_t4 = round(reloj + simulaciones[i].tiempo_registro_huella, 2)
                    simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                    simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                    simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1

            # Si no hay mas empleados en cola
            else:
                simulaciones[i].cola = simulaciones[i - 1].cola
                if simulaciones[i - 1].terminales[int(numero_terminal_fin) - 1].estado == "OR":
                    simulaciones[i].terminales[int(numero_terminal_fin) - 1].estado = "L"

                if numero_terminal_fin == "1":
                    simulaciones[i].fin_registro_huella_t1 = ""
                    simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                    simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                    simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                if numero_terminal_fin == "2":
                    simulaciones[i].fin_registro_huella_t2 = ""
                    simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                    simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                    simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                if numero_terminal_fin == "3":
                    simulaciones[i].fin_registro_huella_t3 = ""
                    simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                    simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
                    simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4

                if numero_terminal_fin == "4":
                    simulaciones[i].fin_registro_huella_t4 = ""
                    simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
                    simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
                    simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1

                simulaciones[i].acumulador_tiempo_espera = simulaciones[i - 1].acumulador_tiempo_espera

            if simulaciones[i - 1].terminales[int(numero_terminal_fin) - 1].estado == "ORM":
                simulaciones[i].terminales[int(numero_terminal_fin) - 1].estado = "OM"

            simulaciones[i].fin_mantenimiento_terminal1 = simulaciones[i-1].fin_mantenimiento_terminal1
            simulaciones[i].fin_mantenimiento_terminal2 = simulaciones[i-1].fin_mantenimiento_terminal2
            simulaciones[i].fin_mantenimiento_terminal3 = simulaciones[i-1].fin_mantenimiento_terminal3
            simulaciones[i].fin_mantenimiento_terminal4 = simulaciones[i-1].fin_mantenimiento_terminal4
            simulaciones[i].mantenimiento_t1 = simulaciones[i-1].mantenimiento_t1
            simulaciones[i].mantenimiento_t2 = simulaciones[i-1].mantenimiento_t2
            simulaciones[i].mantenimiento_t3 = simulaciones[i-1].mantenimiento_t3
            simulaciones[i].mantenimiento_t4 = simulaciones[i-1].mantenimiento_t4
            acumulador_empleados_que_pasan_por_sistema += 1
            simulaciones[i].acumulador_empleados_que_pasaron_por_el_sistema = acumulador_empleados_que_pasan_por_sistema
            simulaciones[i].proxima_llegada_empleado = simulaciones[i - 1].proxima_llegada_empleado
            simulaciones[i].proxima_llegada_tecnico = simulaciones[i - 1].proxima_llegada_tecnico

            # Destruir el empleado que terminó de registrar su huella
            numero_empleado_a_eliminar = simulaciones[i].buscar_empleado(int(numero_terminal_fin))

            if numero_empleado_a_eliminar is not None:
                numero_empleado_a_eliminar = numero_empleado_a_eliminar.get_numero()
                simulaciones[i].eliminar_empleado(numero_empleado_a_eliminar)
            else:
                print(f"No se encontró un empleado en la terminal {numero_terminal_fin}")

        # Si el tecnico termina de hacer mantenimiento a una terminal
        elif evento.startswith("fin_mantenimiento_terminal"):
            numero_terminal_arreglada = int(evento[-2])

            if numero_terminal_arreglada == 1:
                simulaciones[i].mantenimiento_t1 = "SI"

            elif numero_terminal_arreglada == 2:
                simulaciones[i].mantenimiento_t2 = "SI"

            elif numero_terminal_arreglada == 3:
                simulaciones[i].mantenimiento_t3 = "SI"

            elif numero_terminal_arreglada == 4:
                simulaciones[i].mantenimiento_t4 = "SI"

            terminales_restantes = simulaciones[i-1].encontrar_terminales_restantes_a_mantener(numero_terminal_arreglada)

            # Si ya terminó de mantener todas las terminales, se lanza el evento llegada_tecnico de vuelta
            if len(terminales_restantes) == 0:
                pass

            # Si todavia queda 1 o más terminales por mantener
            else:
                pass

            simulaciones[i].proxima_llegada_empleado = simulaciones[i - 1].proxima_llegada_empleado
            simulaciones[i].fin_registro_huella_t1 = simulaciones[i - 1].fin_registro_huella_t1
            simulaciones[i].fin_registro_huella_t2 = simulaciones[i - 1].fin_registro_huella_t2
            simulaciones[i].fin_registro_huella_t3 = simulaciones[i - 1].fin_registro_huella_t3
            simulaciones[i].fin_registro_huella_t4 = simulaciones[i - 1].fin_registro_huella_t4
            simulaciones[i].cola = simulaciones[i - 1].cola
            simulaciones[i].acumulador_tiempo_espera = simulaciones[i - 1].acumulador_tiempo_espera
            simulaciones[i].acumulador_empleados_que_pasaron_por_el_sistema = simulaciones[
                i - 1].acumulador_empleados_que_pasaron_por_el_sistema
            simulaciones[i].acumulador_empleados_que_salen_temporalmente = simulaciones[
                i - 1].acumulador_empleados_que_salen_temporalmente

        t = {
            'llegada_empleado': simulaciones[i].proxima_llegada_empleado if simulaciones[
                                                                                i].proxima_llegada_empleado != "" else float(
                'inf'),
            'llegada_tecnico': simulaciones[i].proxima_llegada_tecnico if simulaciones[
                                                                              i].proxima_llegada_tecnico != "" else float(
                'inf'),
            'fin_registro_huella_t1': simulaciones[i].fin_registro_huella_t1 if simulaciones[
                                                                                    i].fin_registro_huella_t1 != "" else float(
                'inf'),
            'fin_registro_huella_t2': simulaciones[i].fin_registro_huella_t2 if simulaciones[
                                                                                    i].fin_registro_huella_t2 != "" else float(
                'inf'),
            'fin_registro_huella_t3': simulaciones[i].fin_registro_huella_t3 if simulaciones[
                                                                                    i].fin_registro_huella_t3 != "" else float(
                'inf'),
            'fin_registro_huella_t4': simulaciones[i].fin_registro_huella_t4 if simulaciones[
                                                                                    i].fin_registro_huella_t4 != "" else float(
                'inf'),
            'fin_mantenimiento_terminal1': simulaciones[i].fin_mantenimiento_terminal1 if simulaciones[
                                                                                i].fin_mantenimiento_terminal1 != "" else float(
                'inf'),
            'fin_mantenimiento_terminal2': simulaciones[i].fin_mantenimiento_terminal2 if simulaciones[
                                                                                i].fin_mantenimiento_terminal2 != "" else float(
                'inf'),
            'fin_mantenimiento_terminal3': simulaciones[i].fin_mantenimiento_terminal3 if simulaciones[
                                                                                i].fin_mantenimiento_terminal3 != "" else float(
                'inf'),
            'fin_mantenimiento_terminal4': simulaciones[i].fin_mantenimiento_terminal4 if simulaciones[
                                                                                i].fin_mantenimiento_terminal4 != "" else float(
                'inf'),
        }

        menor_tiempo_key = min(t, key=t.get)
        menor_tiempo = t[menor_tiempo_key]
        proximo_evento = menor_tiempo_key

        if proximo_evento.startswith('llegada_empleado'):
            proximo_evento += '(' + str(numero_empleado) + ')'

        elif proximo_evento.startswith('fin_registro_huella'):
            numero_terminal = proximo_evento[-1]
            proximo_evento = proximo_evento[:-3]
            proximo_evento += '(' + numero_terminal + ')'

        elif proximo_evento.startswith('fin_mantenimiento_terminal'):
            numero_terminal = proximo_evento[-1]
            proximo_evento = proximo_evento[:-1]
            proximo_evento += '(' + numero_terminal + ')'

        simulaciones[i].proximo_evento = proximo_evento
        print(simulaciones[i].imprimir_columnas(i))


# PRUEBAS #
minutoARegistroHuella = 5
minutoBRegistroHuella = 8
horaLlegadaTecnico = 1
minutoBLlegadaTecnico = 3
minutoAMantenimientoTerminal = 3
minutoBMantenimientoTerminal = 10
mediaLlegadaEmpleado = 2
iteraciones = 10
cantidad_datos_a_mostrar = ""

simulacion(minutoARegistroHuella, minutoBRegistroHuella, horaLlegadaTecnico, minutoBLlegadaTecnico,
           minutoAMantenimientoTerminal, minutoBMantenimientoTerminal, mediaLlegadaEmpleado,
           iteraciones, cantidad_datos_a_mostrar)