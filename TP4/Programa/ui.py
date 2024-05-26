import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logica import simulacion
import tkinter.font as tkFont

class TablaDatos:
    def __init__(self, datos):
        self.ventana = tk.Tk()
        self.ventana.title("TP Nº4 - SIMULACIÓN - 4K3 - UTN FRC - GRUPO 9")
        self.ventana.geometry("1600x700")
        self.ventana.configure(bg="#f3f3d1")
        self.datos = datos

        self.treeview = ttk.Treeview(self.ventana, columns=(
            "evento", "proximo_evento", "reloj", "rnd_llegada_empleado", "tiempo_entre_llegadas_empleado",
            "proxima_llegada_empleado", "rnd_llegada_tecnico", "tiempo_en_llegar_tecnico", "proxima_llegada_tecnico",
            "rnd_fin_registro_huella", "tiempo_registro_huella", "fin_registro_huella_t1", "fin_registro_huella_t2",
            "fin_registro_huella_t3", "fin_registro_huella_t4", "cola", "rnd_fin_mantenimiento_terminal",
            "tiempo_mantenimiento_terminal", "fin_mantenimiento_t1", "fin_mantenimiento_t2", "fin_mantenimiento_t3",
            "fin_mantenimiento_t4", "acumulador_tiempo_espera", "acumulador_empleados_que_salen",
            "acumulador_empleados_que_pasaron", "estado_tecnico", "mant_t1", "mant_t2", "mant_t3", "mant_t4")
                                     , show="headings")

        self.treeview.heading("evento", text="Evento")
        self.treeview.heading("proximo_evento", text="Próximo Evento")
        self.treeview.heading("reloj", text="Reloj")
        self.treeview.heading("rnd_llegada_empleado", text="RND")
        self.treeview.heading("tiempo_entre_llegadas_empleado", text="Tiempo entre llegadas")
        self.treeview.heading("proxima_llegada_empleado", text="Prox. llegada")
        self.treeview.heading("rnd_llegada_tecnico", text="RND")
        self.treeview.heading("tiempo_en_llegar_tecnico", text="Tiempo llegada")
        self.treeview.heading("proxima_llegada_tecnico", text="Prox. llegada")
        self.treeview.heading("rnd_fin_registro_huella", text="RND")
        self.treeview.heading("tiempo_registro_huella", text="Tiempo Registro")
        self.treeview.heading("fin_registro_huella_t1", text="Fin Registro T1")
        self.treeview.heading("fin_registro_huella_t2", text="Fin Registro T2")
        self.treeview.heading("fin_registro_huella_t3", text="Fin Registro T3")
        self.treeview.heading("fin_registro_huella_t4", text="Fin Registro T4")
        self.treeview.heading("cola", text="Cola")
        self.treeview.heading("rnd_fin_mantenimiento_terminal", text="RND")
        self.treeview.heading("tiempo_mantenimiento_terminal", text="Tiempo Mantenimiento")
        self.treeview.heading("fin_mantenimiento_t1", text="Fin Mantenimiento T1")
        self.treeview.heading("fin_mantenimiento_t2", text="Fin Mantenimiento T2")
        self.treeview.heading("fin_mantenimiento_t3", text="Fin Mantenimiento T3")
        self.treeview.heading("fin_mantenimiento_t4", text="Fin Mantenimiento T4")
        self.treeview.heading("acumulador_tiempo_espera", text="AC Tiempo Espera")
        self.treeview.heading("acumulador_empleados_que_salen", text="AC Empleados que salen")
        self.treeview.heading("acumulador_empleados_que_pasaron", text="AC Empleados que pasaron")
        self.treeview.heading("estado_tecnico", text="Estado Tecnico")
        self.treeview.heading("mant_t1", text="Mantenimiento T1")
        self.treeview.heading("mant_t2", text="Mantenimiento T2")
        self.treeview.heading("mant_t3", text="Mantenimiento T3")
        self.treeview.heading("mant_t4", text="Mantenimiento T4")

        for column in self.treeview["columns"]:
            self.treeview.column(column, width=175, anchor="center")

        self.treeview.pack(expand=True, fill="both")

        xscrollbar = ttk.Scrollbar(self.ventana, orient="horizontal", command=self.treeview.xview)
        xscrollbar.pack(side="bottom", fill="x")
        yscrollbar = tk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview)
        yscrollbar.pack(side="right", fill="y")

        self.treeview.configure(xscrollcommand=xscrollbar.set)
        self.treeview.configure(yscrollcommand=yscrollbar.set)

        for i, obj in enumerate(self.datos, start=0):
            self.treeview.insert("", "end", text=str(i), values=(
                obj.evento, obj.proximo_evento, obj.reloj, obj.rnd_llegada_empleado,
                obj.tiempo_entre_llegadas_empleado, obj.proxima_llegada_empleado,
                obj.rnd_llegada_tecnico, obj.tiempo_en_llegar_tecnico, obj.proxima_llegada_tecnico,
                obj.rnd_fin_registro_huella, obj.tiempo_registro_huella, obj.fin_registro_huella_t1,
                obj.fin_registro_huella_t2, obj.fin_registro_huella_t3, obj.fin_registro_huella_t4,
                obj.cola, obj.rnd_fin_mantenimiento_terminal, obj.tiempo_mantenimiento_terminal,
                obj.fin_mantenimiento_terminal1, obj.fin_mantenimiento_terminal2, obj.fin_mantenimiento_terminal3,
                obj.fin_mantenimiento_terminal4, obj.acumulador_tiempo_espera, obj.acumulador_empleados_que_salen_temporalmente,
                obj.acumulador_empleados_que_pasaron_por_el_sistema, obj.estado_tecnico, obj.mantenimiento_t1,
                obj.mantenimiento_t2, obj.mantenimiento_t3, obj.mantenimiento_t4))

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("TP Nº4 - SIMULACIÓN - 4K3 - UTN FRC - GRUPO 9")
        self.ventana.geometry("1000x320")
        self.ventana.configure(bg="#f3f3d1")

        icon = tk.PhotoImage(file='utn.png')
        self.ventana.iconphoto(False, icon)

        self.label_cantidad_tiempo = tk.Label(text="Cantidad de tiempo (X)", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_cantidad_tiempo.place(x=20, y=20)
        self.entry_cantidad_tiempo = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_cantidad_tiempo.place(x=65, y=50)

        self.label_minuto_desde = tk.Label(text="Minuto desde (i)", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_minuto_desde.place(x=50, y=80)
        self.entry_minuto_desde = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_desde.place(x=65, y=110)

        self.label_minuto_hasta = tk.Label(text="Minuto hasta (j)", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_minuto_hasta.place(x=50, y=140)
        self.entry_minuto_hasta = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_hasta.place(x=65, y=170)

        # MEDIO DE LA VENTANA #
        self.label_evento_llegada_empleado = tk.Label(text="Evento llegada_empleado", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_evento_llegada_empleado.place(x=300, y=20)
        self.entry_media_evento_llegada_empleado = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_media_evento_llegada_empleado.place(x=350, y=50)
        self.label_media_llegada_empleado = tk.Label(text="Media", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_media_llegada_empleado.place(x=460, y=50)

        self.label_evento_llegada_tecnico = tk.Label(text="Evento llegada_tecnico", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_evento_llegada_tecnico.place(x=300, y=110)
        self.label_hora_A_llegada_tecnico = tk.Label(text="A (en horas)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_hora_A_llegada_tecnico.place(x=460, y=140)
        self.entry_hora_A_llegada_tecnico = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_hora_A_llegada_tecnico.place(x=350, y=140)
        self.label_minuto_B_llegada_tecnico = tk.Label(text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_B_llegada_tecnico.place(x=460, y=170)
        self.entry_minuto_B_llegada_tecnico = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_B_llegada_tecnico.place(x=350, y=170)

        # DERECHO DE LA VENTANA #
        self.label_evento_fin_registro_huella = tk.Label(text="Evento fin_registro_huella", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_evento_fin_registro_huella.place(x=600, y=20)
        self.entry_minuto_A_fin_registro_huella = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_A_fin_registro_huella.place(x=650, y=50)
        self.label_minuto_A_fin_registro_huella = tk.Label(text="A (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_A_fin_registro_huella.place(x=750, y=50)
        self.entry_minuto_B_fin_registro_huella = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_B_fin_registro_huella.place(x=650, y=80)
        self.label_minuto_B_fin_registro_huella = tk.Label(text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_B_fin_registro_huella.place(x=750, y=80)

        self.label_evento_fin_mantenimiento_terminal = tk.Label(text="Evento fin_mantenimiento_terminal", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_evento_fin_mantenimiento_terminal.place(x=600, y=110)
        self.entry_minuto_A_fin_mantenimiento_terminal = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_A_fin_mantenimiento_terminal.place(x=650, y=140)
        self.label_minuto_A_fin_mantenimiento_terminal = tk.Label(text="A (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_A_fin_mantenimiento_terminal.place(x=750, y=140)
        self.entry_minuto_B_fin_mantenimiento_terminal = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_B_fin_mantenimiento_terminal.place(x=650, y=170)
        self.label_minuto_B_fin_mantenimiento_terminal = tk.Label(text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_B_fin_mantenimiento_terminal.place(x=750, y=170)

        self.button = tk.Button(text="Generar simulación", font=("Consolas", 16, "bold"), bg="lightblue", fg="black", command=self.validacion_datos)
        self.button.place(x=360, y=250, width=300, height=50)

    def validacion_datos(self):
        try:
            '''cantidad_tiempo = float(self.entry_cantidad_tiempo.get())
            minuto_desde = float(self.entry_minuto_desde.get())
            minuto_hasta = float(self.entry_minuto_hasta.get())
            media_llegada_empleado = float(self.entry_media_evento_llegada_empleado.get())
            hora_A_llegada_tecnico = float(self.entry_hora_A_llegada_tecnico.get())
            minuto_B_llegada_tecnico = float(self.entry_minuto_B_llegada_tecnico.get())
            minuto_A_fin_registro_huella = float(self.entry_minuto_A_fin_registro_huella.get())
            minuto_B_fin_registro_huella = float(self.entry_minuto_B_fin_registro_huella.get())
            minuto_A_fin_mantenimiento_terminal = float(self.entry_minuto_A_fin_mantenimiento_terminal.get())
            minuto_B_fin_mantenimiento_terminal = float(self.entry_minuto_B_fin_mantenimiento_terminal.get())'''

            minuto_A_fin_registro_huella = 5
            minuto_B_fin_registro_huella = 8
            hora_A_llegada_tecnico = 1
            minuto_B_llegada_tecnico = 3
            minuto_A_fin_mantenimiento_terminal = 3
            minuto_B_fin_mantenimiento_terminal = 10
            media_llegada_empleado = 2
            cantidad_tiempo = 1
            minuto_desde = 1
            minuto_hasta = 2

            minuto_B_es_correcto = True if (hora_A_llegada_tecnico*60-minuto_B_llegada_tecnico >= 0) else False

            if cantidad_tiempo > 0:
                if minuto_desde >= 0:
                    if minuto_hasta > 0 and minuto_hasta > minuto_desde:
                        if media_llegada_empleado > 0:
                            if hora_A_llegada_tecnico >= 0 and minuto_B_es_correcto:
                                if minuto_A_fin_registro_huella >= 0 and minuto_B_fin_registro_huella >= 0 and minuto_B_fin_registro_huella > minuto_A_fin_registro_huella:
                                    if minuto_A_fin_mantenimiento_terminal >= 0 and minuto_B_fin_mantenimiento_terminal >= 0 and minuto_B_fin_mantenimiento_terminal > minuto_A_fin_mantenimiento_terminal:
                                        # Llamar a Simulacion
                                        '''# ESTO ES PARA PROBAR CON LA INTERFAZ
                                        datos = simulacion(minutoARegistroHuella=minuto_A_fin_registro_huella,
                                                           minutoBRegistroHuella=minuto_B_fin_registro_huella,
                                                           mediaLlegadaEmpleado=media_llegada_empleado,
                                                           horaALlegadaTecnico=hora_A_llegada_tecnico,
                                                           minutoBLlegadaTecnico=minuto_B_llegada_tecnico,
                                                           minutoAMantenimientoTerminal=minuto_A_fin_mantenimiento_terminal,
                                                           minutoBMantenimientoTerminal=minuto_B_fin_mantenimiento_terminal,
                                                           )'''
                                        # PRUEBAS SIN INGRESO DE DATOS POR INTERFAZ #
                                        datos = simulacion(minutoARegistroHuella=minuto_A_fin_registro_huella,
                                                           minutoBRegistroHuella=minuto_B_fin_registro_huella,
                                                           mediaLlegadaEmpleado=media_llegada_empleado,
                                                           horaALlegadaTecnico=hora_A_llegada_tecnico,
                                                           minutoBLlegadaTecnico=minuto_B_llegada_tecnico,
                                                           minutoAMantenimientoTerminal=minuto_A_fin_mantenimiento_terminal,
                                                           minutoBMantenimientoTerminal=minuto_B_fin_mantenimiento_terminal,
                                                           cantidad_tiempo=cantidad_tiempo,
                                                           minuto_desde=minuto_desde,
                                                           minuto_hasta=minuto_hasta
                                                           )
                                        # Crear la tabla

                                        TablaDatos(datos)

            else:
                messagebox.showerror("Error", "Ha ingresado algún dato erróneo. Revise de vuelta")
                return

        except ValueError:
            messagebox.showerror("Error", "Se detectó un ingreso de caracter inválido.")
