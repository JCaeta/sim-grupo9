from Distribuciones import DistribucionLlegadaTecnico, DistribucionLlegadaEmpleado, DistribucionFinRegistroHuella, DistribucionFinMantenimientoTerminal
from Objetos import Empleado, Tecnico
from Objetos import Terminal as T
from Simulacion import EventosYAuxiliares
from utilidades import *

def simulacion(minutoARegistroHuella, minutoBRegistroHuella,
                   minutoALlegadaTecnico, minutoBLlegadaTecnico,
                   minutoAMantenimientoTerminal, minutoBMantenimientoTerminal,
                   mediaLlegadaEmpleado, iteraciones, cantidad_datos_a_mostrar):

    ######## INICIALIZACIÓN DE CADA DISTRIBUCIÓN ##########

    dist_registro_huella = DistribucionFinRegistroHuella.DistribucionFinRegistroHuella(a=minutoARegistroHuella,
                                                                                       b=minutoBRegistroHuella)

    dist_tecnico = DistribucionLlegadaTecnico.DistribucionLlegadaTecnico(a=minutoALlegadaTecnico,
                                                                         b=minutoBLlegadaTecnico)

    dist_mantenimiento_terminal = (DistribucionFinMantenimientoTerminal.
                                   DistribucionFinMantenimientoTerminal(a=minutoAMantenimientoTerminal,
                                                                        b=minutoBMantenimientoTerminal))

    dist_llegada_empleado = DistribucionLlegadaEmpleado.DistribucionLlegadaEmpleado(media=mediaLlegadaEmpleado)

    ############################################################

    simulaciones = []
    empleados = []
    terminales = [
        {T.Terminal(numero=1, estado="L")},
        {T.Terminal(numero=2, estado="L")},
        {T.Terminal(numero=3, estado="L")},
        {T.Terminal(numero=4, estado="L")}
    ]
    evento = "Inicialización"
    proximo_evento = ""
    reloj = 0.00
    tecnico = Tecnico.Tecnico(estado="L")
    estado_tecnico = tecnico.get_estado()
    numero_empleado = 0
    numero_terminal = 0
    cola = 0

    for i in range(iteraciones):
        # if proximo_evento == llegada_empleado
        rnd_llegada_empleado = rnd()
        tiempo_entre_llegadas_empleado = generador_exponencial(media=dist_llegada_empleado.get_media(),
                                                               random=rnd_llegada_empleado)
        proxima_llegada_empleado = reloj + tiempo_entre_llegadas_empleado

        rnd_llegada_tecnico = rnd()
        tiempo_entre_llegar_tecnico = generador_uniforme(a=dist_tecnico.get_a(),
                                                         b=dist_tecnico.get_b(),
                                                         random=rnd_llegada_tecnico)
        # if proximo_evento == llegada_tecnico
        proxima_llegada_tecnico = reloj + tiempo_entre_llegar_tecnico

        # if proximo_evento == llegada_empleado and cola == 0:
        #
        # rnd_fin_registro_huella = rnd()
        # tiempo_registro_huella = generador_uniforme(a=dist_registro_huella.get_a(),
        #                                            b=dist_registro_huella.get_b(),
        #                                            random=rnd_fin_registro_huella)

        # ACA IRÍA EL TIEMPO QUE TARDARÍA CADA TERMINAL SEGÚN SEA EL CASO
        # if proximo_evento == fin_registro_huella and cola > 0:
        #       if terminal == 1:
        #           fin_registro_huella_t1 = reloj + tiempo_registro_huella
        #       if terminal == 2:
        #           fin_registro_huella_t1 = reloj + tiempo_registro_huella
        #       if terminal == 3:
        #           fin_registro_huella_t1 = reloj + tiempo_registro_huella
        #       if terminal == 4:
        #           fin_registro_huella_t1 = reloj + tiempo_registro_huella

        # if proximo_evento == llegada_tecnico or proximo_evento == fin_mantenimiento_terminal
        # rnd_fin_mantenimiento_terminal = rnd()
        # tiempo_mantenimiento_terminal = generador_uniforme(a=dist_mantenimiento_terminal.get_a(),
        #                                                   b=dist_mantenimiento_terminal.get_b(),
        #                                                   random=rnd_fin_mantenimiento_terminal)
        # Determinar a qué terminal ir, viendo primero la/s que esté/n libre/s,
        # y luego al azar ir eligiendo hasta terminar

        # tecnico.set_estado(estado = "RM")
        # estado_tecnico = tecnico.get_estado()

        # Aca se crearian las columnas para los empleados
        # if proximo_evento == llegada_empleado:
        #   numero_empleado += 1
        #   if cola > 5:
        #       estado_empleado = "ST"
        #       minuto_salida_temporalmente = reloj
        #   elif cola <= 5 and todas las terminales ocupadas:
        #       estado_empleado = "EC"
        #       minuto_entrada_cola = reloj
        #   else:
        #       estado_empleado = "HR" + Nro. de terminal en la que está haciendo el registro
        #   Empleado.Empleado(numero=numero_empleado, estado="...",
        #                   minuto_salida_temporalmente="...",
        #                   minuto_entrada_cola="...")

