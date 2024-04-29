import tkinter as tk
from tkinter import ttk, messagebox
from logica import simulacion, Parametros


class MainWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Ingreso de iteraciones")
        self.geometry("600x400")
        self.configure(bg="#ffffe6")

        self.label_dias = tk.Label(self,
                                   text="Ingrese la cantidad de días a simular (1-100.000):",
                                   font=("Arial", 14),
                                   bg="#ffffe6")

        self.label_dias.place(relx=0.2, rely=0.2)

        self.tamaño_entry = tk.Entry(self)
        self.tamaño_entry.place(relx=0.35, rely=0.3)

        self.label_obreros = tk.Label(self,
                                      text="Seleccione la nómina de obreros:",
                                      font=("Arial", 14),
                                      bg="#ffffe6")

        self.label_obreros.place(relx=0.24, rely=0.4)

        self.obreros_combobox = ttk.Combobox(self, values=[24, 23, 22, 21], state="readonly")
        self.obreros_combobox.place(relx=0.35, rely=0.5)

        self.ok_button = tk.Button(self,
                                   text="Confirmar datos",
                                   command=self.validacion_datos,
                                   width=12,
                                   height=2,
                                   font=("Arial", 12), bg="#99ffcc")

        self.ok_button.place(relx=0.37, rely=0.65)

    def validacion_datos(self):
        try:
            dias = int(self.tamaño_entry.get())
            obreros = int(self.obreros_combobox.get())

            if 1 <= dias <= 100000:
                self.master.withdraw()
                SimulacionWindow(self.master, dias, obreros)

            else:
                messagebox.showerror("Error", "La cantidad de días de la simulación tiene que estar entre 1 y 100.000")
                return

        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")


class SimulacionWindow(tk.Toplevel):
    distribucion_window_instance = None

    def __init__(self, parent, dias, obreros):
        super().__init__(parent)

        self.title("Simulación")
        self.geometry("1600x900")
        self.configure(bg="#ffffe6")

        self.label_ingresos_por_venta = tk.Label(self,
                                                 text="Ingresos por venta:",
                                                 font=("Arial", 12, "bold"),
                                                 bg="#ffffe6")

        self.label_ingresos_por_venta.place(relx=0.05, rely=0.05)

        self.ingresos_por_venta_entry = tk.Entry(self)
        self.ingresos_por_venta_entry.place(relx=0.05, rely=0.1)

        self.label_costos_por_venta = tk.Label(self,
                                               text="Costos por venta:",
                                               font=("Arial", 12, "bold"),
                                               bg="#ffffe6")

        self.label_costos_por_venta.place(relx=0.05, rely=0.2)

        self.costos_por_venta_entry = tk.Entry(self)
        self.costos_por_venta_entry.place(relx=0.05, rely=0.25)

        self.label_remuneracion_obrero = tk.Label(self,
                                                  text="Costos de remuneración por obrero:",
                                                  font=("Arial", 12, "bold"),
                                                  bg="#ffffe6")

        self.label_remuneracion_obrero.place(relx=0.05, rely=0.35)

        self.remuneracion_obrero_entry = tk.Entry(self)
        self.remuneracion_obrero_entry.place(relx=0.05, rely=0.4)

        # Labels y entries de día desde y día hasta (derecha arriba)
        self.label_dia_desde = tk.Label(self,
                                        text="Desde qué día:",
                                        font=("Arial", 12, "bold"),
                                        bg="#ffffe6")

        self.label_dia_desde.place(relx=0.75, rely=0.15)

        self.rango_desde_entry = tk.Entry(self)
        self.rango_desde_entry.place(relx=0.75, rely=0.20)

        self.label_cantidad_datos = tk.Label(self,
                                             text="Cuantos días más?:",
                                             font=("Arial", 12, "bold"),
                                             bg="#ffffe6")

        self.label_cantidad_datos.place(relx=0.75, rely=0.25)

        self.cantidad_datos_entry = tk.Entry(self)
        self.cantidad_datos_entry.place(relx=0.75, rely=0.30)

        # Labels y entries de obreros (medio arriba)
        self.label_frecuencia = tk.Label(self,
                                         text="Cantidad de veces que se ausentaron los obreros en 100 días:",
                                         font=("Arial", 12, "bold"),
                                         bg="#ffffe6")

        self.label_frecuencia.place(relx=0.35, rely=0.05)

        self.label_frecuencia_obrero_cero = tk.Label(self,
                                                     text="0 obreros",
                                                     bg="#ffffe6",
                                                     font=("Arial", 10, "bold"))

        self.label_frecuencia_obrero_cero.place(relx=0.4, rely=0.1)

        self.frecuencia_obrero_cero_entry = tk.Entry(self, width=5)
        self.frecuencia_obrero_cero_entry.place(relx=0.47, rely=0.1)

        self.label_frecuencia_obrero_uno = tk.Label(self,
                                                    text="1 obrero",
                                                    bg="#ffffe6",
                                                    font=("Arial", 10, "bold"))
        self.label_frecuencia_obrero_uno.place(relx=0.4, rely=0.15)

        self.frecuencia_obrero_uno_entry = tk.Entry(self, width=5)
        self.frecuencia_obrero_uno_entry.place(relx=0.47, rely=0.15)

        self.label_frecuencia_obrero_dos = tk.Label(self,
                                                    text="2 obreros",
                                                    bg="#ffffe6",
                                                    font=("Arial", 10, "bold"))
        self.label_frecuencia_obrero_dos.place(relx=0.4, rely=0.2)

        self.frecuencia_obrero_dos_entry = tk.Entry(self, width=5)
        self.frecuencia_obrero_dos_entry.place(relx=0.47, rely=0.2)

        self.label_frecuencia_obrero_tres = tk.Label(self,
                                                     text="3 obreros",
                                                     bg="#ffffe6",
                                                     font=("Arial", 10, "bold"))
        self.label_frecuencia_obrero_tres.place(relx=0.4, rely=0.25)

        self.frecuencia_obrero_tres_entry = tk.Entry(self, width=5)
        self.frecuencia_obrero_tres_entry.place(relx=0.47, rely=0.25)

        self.label_frecuencia_obrero_cuatro = tk.Label(self,
                                                       text="4 obreros",
                                                       bg="#ffffe6",
                                                       font=("Arial", 10, "bold"))
        self.label_frecuencia_obrero_cuatro.place(relx=0.4, rely=0.3)

        self.frecuencia_obrero_cuatro_entry = tk.Entry(self, width=5)
        self.frecuencia_obrero_cuatro_entry.place(relx=0.47, rely=0.3)

        self.label_frecuencia_obrero_cinco = tk.Label(self,
                                                      text="5 o más obreros",
                                                      bg="#ffffe6",
                                                      font=("Arial", 10, "bold"))
        self.label_frecuencia_obrero_cinco.place(relx=0.4, rely=0.35)

        self.frecuencia_obrero_cinco_entry = tk.Entry(self, width=5)
        self.frecuencia_obrero_cinco_entry.place(relx=0.47, rely=0.35)

        self.ok_button = tk.Button(self,
                                   text="Validar",
                                   command=lambda: self.mostrar_datos(dias, obreros),
                                   width=20,
                                   bg="#99ffcc",
                                   font=("Arial", 10, "bold"))

        self.ok_button.place(relx=0.45, rely=0.45)

        self.generar_distribucion_button = tk.Button(self,
                                                     text="Generar Distribución de Frecuencias",
                                                     command=self.generar_distribucion,
                                                     width=30,
                                                     state="disabled",
                                                     bg="#99ffcc",
                                                     font=("Arial", 10, "bold"))

        self.generar_distribucion_button.place(relx=0.425, rely=0.5)

        self.treeview = ttk.Treeview(self, columns=(
            "dia", "rnd_obrero", "obreros_ausentes", "obreros_presentes", "planta_operable", "beneficio",
            "beneficio_acumulado"), show="headings")

        self.treeview.heading("dia", text="Día")
        self.treeview.heading("rnd_obrero", text="RND Obrero")
        self.treeview.heading("obreros_ausentes", text="Obreros Ausentes")
        self.treeview.heading("obreros_presentes", text="Obreros Presentes")
        self.treeview.heading("planta_operable", text="Planta Operable")
        self.treeview.heading("beneficio", text="Beneficio $")
        self.treeview.heading("beneficio_acumulado", text="Beneficio Acumulado $")

        self.treeview.column("dia", width=5, anchor="center")
        self.treeview.column("rnd_obrero", width=5, anchor="center")
        self.treeview.column("obreros_ausentes", width=5, anchor="center")
        self.treeview.column("obreros_presentes", width=5, anchor="center")
        self.treeview.column("planta_operable", width=5, anchor="center")
        self.treeview.column("beneficio", width=15, anchor="center")
        self.treeview.column("beneficio_acumulado", width=15, anchor="center")

        self.treeview.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.3)

        scrollbar = tk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")

        self.treeview.configure(yscrollcommand=scrollbar.set)

    def mostrar_datos(self, dias, obreros):
        try:
            rango_desde = int(self.rango_desde_entry.get())
            cantidad_datos = int(self.cantidad_datos_entry.get())
            ingresos_venta = float(self.ingresos_por_venta_entry.get())
            costos_venta = float(self.costos_por_venta_entry.get())
            remuneracion_obrero = float(self.remuneracion_obrero_entry.get())

            frecuencias = [self.frecuencia_obrero_cero_entry.get(),
                           self.frecuencia_obrero_uno_entry.get(),
                           self.frecuencia_obrero_dos_entry.get(),
                           self.frecuencia_obrero_tres_entry.get(),
                           self.frecuencia_obrero_cuatro_entry.get(),
                           self.frecuencia_obrero_cinco_entry.get(), ]

            if cantidad_datos > dias or rango_desde > dias or rango_desde < 0 or cantidad_datos < 0 or (
                    cantidad_datos + rango_desde) > dias:
                messagebox.showerror("Error", "Rango invalido")
                return

            if ingresos_venta < 0 or costos_venta < 0 or remuneracion_obrero < 0:
                messagebox.showerror("Error", "No se pueden ingresar valores negativos")
                return

            for i in frecuencias:
                if not i.isdigit():
                    messagebox.showerror("Error", "Ingresó alguna frecuencia que no es entera o positiva")
                    return

            lista_frecuencias = list(map(int, frecuencias))

            if sum(lista_frecuencias) != 100:
                messagebox.showerror("Revisar", "La suma de las frecuencias debe ser igual a 100.")
                return

            objeto_parametros = Parametros(ingresos_venta=ingresos_venta,
                                           costo_venta=costos_venta,
                                           remuneracion_obrero=remuneracion_obrero)

            objeto_parametros.setear_probabilidades(lista_frecuencias)

            self.distribucion_frecuencias = objeto_parametros.getDistribucionFrecuencia()
            self.generar_distribucion_button["state"] = "normal"

            self.treeview.delete(*self.treeview.get_children())  # Limpiar la tabla

            lista = simulacion(dias, obreros, rango_desde, cantidad_datos, objeto_parametros)

            for i, obj in enumerate(lista, start=0):
                self.treeview.insert("", "end", text=str(i), values=(
                    obj.get_dia(), obj.get_rnd_obrero(), obj.get_obreros_ausentes(),
                    obj.get_obreros_presentes(),
                    obj.get_planta_operable(), '$' + str(round((obj.get_beneficio()), 4)), '$' +
                    str(round((obj.get_beneficio_acumulado()), 4))))

            self.label_beneficio_total = tk.Label(self,
                                                  text=f"Beneficio total: ${round((lista[-1].get_beneficio_acumulado()), 4)}",
                                                  font=("Arial", 12, "bold"),
                                                  bg="#99ffcc")

            self.label_beneficio_total.place(relx=0.45, rely=0.9)

        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")

    def generar_distribucion(self):
        if self.distribucion_window_instance is None or not self.distribucion_window_instance.winfo_exists():
            self.distribucion_window_instance = DistribucionWindow(self, self.distribucion_frecuencias)
        else:
            self.distribucion_window_instance.lift()


class DistribucionWindow(tk.Toplevel):

    def __init__(self, master, distribucion):
        super().__init__(master)
        self.title("Distribución de Frecuencia")
        self.geometry("800x200")
        self.configure(bg="#ffffe6")

        self.treeview = ttk.Treeview(self, columns=(
            "num_obreros_ausentes", "frecuencia", "probabilidad", "probabilidad_acumulada"), show="headings")
        self.treeview.heading("num_obreros_ausentes", text="Nº Obreros Ausentes")
        self.treeview.heading("frecuencia", text="Frecuencia")
        self.treeview.heading("probabilidad", text="Probabilidad")
        self.treeview.heading("probabilidad_acumulada", text="Probabilidad Acumulada")

        self.treeview.column("num_obreros_ausentes", width=150, anchor="center")
        self.treeview.column("frecuencia", width=150, anchor="center")
        self.treeview.column("probabilidad", width=150, anchor="center")
        self.treeview.column("probabilidad_acumulada", width=150, anchor="center")

        for item in distribucion:
            if item[0] == 5:
                item = (["5 o más"]) + item[1:]
            self.treeview.insert("", "end", values=item)

        self.treeview.pack(fill="both", expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trabajo Práctico N.º3")
        self.geometry("500x300")
        self.configure(bg="#ffffe6")

        self.generate_button = tk.Button(self,
                                         text="Comenzar",
                                         command=self.open_main_window,
                                         width=15,
                                         height=5,
                                         bg="#99ffcc",
                                         font=("Arial", 10, "bold"))

        self.generate_button.place(relx=0.5, rely=0.5, anchor="center")

    def open_main_window(self):
        MainWindow(self)
