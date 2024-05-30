import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logica import simulacion
import pandas as pd
from tksheet import Sheet


class TablaPandas:
    def __init__(self, simulaciones):
        self.datos = [sim.to_dict() for sim in simulaciones]
        # Convertir la instancia de Simulacion a un diccionario y luego a un DataFrame
        df = pd.DataFrame(self.datos)

        # Crear la ventana principal
        root = tk.Tk()
        root.title("Tabla de Simulación")

        # Crear el widget Sheet
        sheet = Sheet(root,
                      data=df.values.tolist(),  # Convertir el DataFrame a una lista de listas
                      headers=list(df.columns),  # Usar los nombres de las columnas del DataFrame como encabezados
                      width=1000,
                      height=400,
                      column_width=200)



        sheet.enable_bindings("single_select",
                              "row_select",
                              "column_width_resize",
                              "arrowkeys",
                              "right_click_popup_menu",
                              "rc_select",
                              "copy",
                              "cut",
                              "paste",
                              "delete",
                              "undo")

        for _ in df.columns:
            sheet.align(align="center")

        # Empaquetar el widget Sheet
        sheet.pack(expand=True, fill='both')


class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("TP Nº4 - SIMULACIÓN - 4K3 - UTN FRC - GRUPO 9")
        self.ventana.geometry("1000x320")
        self.ventana.configure(bg="#f3f3d1")

        icon = tk.PhotoImage(file='utn.png')
        self.ventana.iconphoto(False, icon)

        self.label_cantidad_tiempo = tk.Label(text="Cantidad de tiempo (X)", font=("Helvetica", 14, "bold"),
                                              bg='#f3f3d1')
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
        self.label_evento_llegada_empleado = tk.Label(text="Evento llegada_empleado", font=("Helvetica", 14, "bold"),
                                                      bg='#f3f3d1')
        self.label_evento_llegada_empleado.place(x=300, y=20)
        self.entry_media_evento_llegada_empleado = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_media_evento_llegada_empleado.place(x=350, y=50)
        self.label_media_llegada_empleado = tk.Label(text="Media", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_media_llegada_empleado.place(x=460, y=50)

        self.label_evento_llegada_tecnico = tk.Label(text="Evento llegada_tecnico", font=("Helvetica", 14, "bold"),
                                                     bg='#f3f3d1')
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
        self.label_evento_fin_registro_huella = tk.Label(text="Evento fin_registro_huella",
                                                         font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_evento_fin_registro_huella.place(x=600, y=20)
        self.entry_minuto_A_fin_registro_huella = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_A_fin_registro_huella.place(x=650, y=50)
        self.label_minuto_A_fin_registro_huella = tk.Label(text="A (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_A_fin_registro_huella.place(x=750, y=50)
        self.entry_minuto_B_fin_registro_huella = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_B_fin_registro_huella.place(x=650, y=80)
        self.label_minuto_B_fin_registro_huella = tk.Label(text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
        self.label_minuto_B_fin_registro_huella.place(x=750, y=80)

        self.label_evento_fin_mantenimiento_terminal = tk.Label(text="Evento fin_mantenimiento_terminal",
                                                                font=("Helvetica", 14, "bold"), bg='#f3f3d1')
        self.label_evento_fin_mantenimiento_terminal.place(x=600, y=110)
        self.entry_minuto_A_fin_mantenimiento_terminal = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_A_fin_mantenimiento_terminal.place(x=650, y=140)
        self.label_minuto_A_fin_mantenimiento_terminal = tk.Label(text="A (en minutos)", font=("Helvetica", 12),
                                                                  bg='#f3f3d1')
        self.label_minuto_A_fin_mantenimiento_terminal.place(x=750, y=140)
        self.entry_minuto_B_fin_mantenimiento_terminal = tk.Entry(font=("Helvetica", 12), width=10)
        self.entry_minuto_B_fin_mantenimiento_terminal.place(x=650, y=170)
        self.label_minuto_B_fin_mantenimiento_terminal = tk.Label(text="B (en minutos)", font=("Helvetica", 12),
                                                                  bg='#f3f3d1')
        self.label_minuto_B_fin_mantenimiento_terminal.place(x=750, y=170)

        self.button = tk.Button(text="Generar simulación", font=("Consolas", 16, "bold"),
                                bg="lightblue", fg="black", command=self.validacion_datos)
        self.button.place(x=360, y=250, width=300, height=50)

    def validacion_datos(self):
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
        TablaPandas(datos)

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



            minuto_B_es_correcto = True if (hora_A_llegada_tecnico * 60 - minuto_B_llegada_tecnico >= 0) else False

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
                                        pass

            else:
                messagebox.showerror("Error", "Ha ingresado algún dato erróneo. Revise de vuelta")
                return

        except ValueError:
            messagebox.showerror("Error", "Se detectó un ingreso de caracter inválido.")
