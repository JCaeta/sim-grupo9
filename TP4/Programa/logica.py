import random

from Distribuciones import DistribucionLlegadaTecnico, DistribucionLlegadaEmpleado, DistribucionFinRegistroHuella, DistribucionFinMantenimientoTerminal
from Objetos import Empleado, Tecnico
from Objetos import Terminal as T
from Simulacion import Simulacion
from utilidades import *


def simulacion(minutoARegistroHuella, minutoBRegistroHuella,
               minutoALlegadaTecnico, minutoBLlegadaTecnico,
               minutoAMantenimientoTerminal, minutoBMantenimientoTerminal,
               mediaLlegadaEmpleado, iteraciones, cantidad_datos_a_mostrar):

    # EVENTOS #
    def llegada_empleado(num_empleado, reloj, cola):
        rnd_llegada_empleado = rnd()
        tiempo_entre_llegadas_empleado = generador_exponencial(media=dist_llegada_empleado.get_media(),
                                                               random=rnd_llegada_empleado)
        proxima_llegada_empleado = reloj + tiempo_entre_llegadas_empleado
        if cola > 5:
            estado_empleado = "ST"
            Empleado.Empleado(numero=num_empleado,
                              estado=estado_empleado,
                              minuto_regreso=reloj+30,
                              minuto_entrada_cola="",
                              terminal="")
            return "regreso_cliente" + '(' + str(
                num_empleado) + ')', rnd_llegada_empleado, tiempo_entre_llegadas_empleado, proxima_llegada_empleado
        hay_terminal_libre = False
        numero_terminal = ""
        for t in terminales:
            if t.get_estado() == "L":
                numero_terminal = t.get_numero()
                hay_terminal_libre = True
                break

        if hay_terminal_libre:
            estado_empleado = "HR" + '(' + str(numero_terminal) + ')'
            Empleado.Empleado(numero=num_empleado,
                              estado=estado_empleado,
                              minuto_regreso="",
                              minuto_entrada_cola="",
                              terminal=numero_terminal)

        else:
            estado_empleado = "EC"
            Empleado.Empleado(numero=num_empleado,
                              estado=estado_empleado,
                              minuto_entrada_cola=reloj,
                              minuto_regreso="",
                              terminal="")
            cola += 1

        return "llegada_empleado" + '(' + str(num_empleado) + ')', rnd_llegada_empleado, tiempo_entre_llegadas_empleado, proxima_llegada_empleado

    def llegada_tecnico(reloj):
        rnd_llegada_tecnico = rnd()
        tiempo_entre_llegar_tecnico = generador_uniforme(a=dist_tecnico.get_a(),
                                                         b=dist_tecnico.get_b(),
                                                         random=rnd_llegada_tecnico)
        tiempo_llegada_tecnico = reloj + tiempo_entre_llegar_tecnico

        return "llegada_tecnico", rnd_llegada_tecnico, tiempo_entre_llegar_tecnico, tiempo_llegada_tecnico

    def fin_registro_huella(emp, nro_terminal, cola, reloj):
        rnd_fin_registro_huella = rnd()
        tiempo_registro_huella = generador_uniforme(a=dist_registro_huella.get_a(),
                                                    b=dist_registro_huella.get_b(),
                                                    random=rnd_fin_registro_huella)
        terminal_ocupada_por_empleado = emp.get_terminal()

        fin_registro_huella_terminal = ""

        if terminal_ocupada_por_empleado != "":
            terminales[terminal_ocupada_por_empleado - 1].estado = "OR"
            fin_registro_huella_terminal = tiempo_registro_huella + reloj

            if cola > 0:
                cola -= 1

        else:
            terminales[nro_terminal - 1].estado = "L"

        return ("fin_registro_huella" + '(T:' + nro_terminal + ',C:' + str(emp.get_numero()),
                rnd_fin_registro_huella,
                tiempo_registro_huella,
                fin_registro_huella_terminal)

    def fin_mantenimiento_terminal(reloj, nro_terminal):
        rnd_fin_mantenimiento_terminal = rnd()
        tiempo_mantenimiento_terminal = generador_uniforme(a=dist_mantenimiento_terminal.get_a(),
                                                           b=dist_mantenimiento_terminal.get_b(),
                                                           random=rnd_fin_mantenimiento_terminal)
        if terminales[nro_terminal - 1].estado == "L":
            terminales[nro_terminal - 1].estado = "OM"

        elif terminales[nro_terminal - 1].estado == "OR":
            terminales[nro_terminal - 1].estado = "ORM"

        fin_mantenimiento_t = reloj + tiempo_mantenimiento_terminal
        return ("fin_mantenimiento_terminal" + '(' + str(nro_terminal) + ')' + rnd_fin_mantenimiento_terminal,
                tiempo_mantenimiento_terminal, fin_mantenimiento_t)

    ###########

    ######## INICIALIZACIÓN DE CADA DISTRIBUCIÓN ##########

    dist_registro_huella = DistribucionFinRegistroHuella.DistribucionFinRegistroHuella(a=minutoARegistroHuella,
                                                                                       b=minutoBRegistroHuella)

    dist_tecnico = DistribucionLlegadaTecnico.DistribucionLlegadaTecnico(a=minutoALlegadaTecnico*60,
                                                                         b=minutoBLlegadaTecnico)

    dist_mantenimiento_terminal = (DistribucionFinMantenimientoTerminal.
                                   DistribucionFinMantenimientoTerminal(a=minutoAMantenimientoTerminal,
                                                                        b=minutoBMantenimientoTerminal))

    dist_llegada_empleado = DistribucionLlegadaEmpleado.DistribucionLlegadaEmpleado(media=mediaLlegadaEmpleado)

    ############################################################












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