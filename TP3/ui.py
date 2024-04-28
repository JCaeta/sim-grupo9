import tkinter as tk
from tkinter import ttk, messagebox
from logica import simulacion, Parametros


class MainWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Ingreso de iteraciones")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Ingrese la cantidad de días a simular (1-100.000):")
        self.label.pack()

        self.tamaño_entry = tk.Entry(self)
        self.tamaño_entry.pack()

        self.label_obreros = tk.Label(self, text="Seleccione la nómina de obreros:")
        self.label_obreros.pack()

        self.obreros_combobox = ttk.Combobox(self, values=[24, 23, 22, 21], state="readonly")
        self.obreros_combobox.pack()

        self.ok_button = tk.Button(self, text="OK", command=self.validacion_datos)
        self.ok_button.pack()

    def validacion_datos(self):
        try:
            dias = int(self.tamaño_entry.get())
            obreros = int(self.obreros_combobox.get())
            if 1 <= dias <= 100000:
                self.master.withdraw()
                SimulacionWindow(self.master, dias, obreros)
            else:
                messagebox.showerror("Error", "La cantidad de días de la simulación tiene que estar entre 1 y 100.000")
        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")


class SimulacionWindow(tk.Toplevel):
    def __init__(self, parent, dias, obreros):
        super().__init__(parent)
        self.title("Simulación")
        self.geometry("1600x900")


        self.label_ingresos_por_venta = tk.Label(self, text="Ingresos por venta:")
        self.label_ingresos_por_venta.place(relx=0.05, rely=0.05)

        self.ingresos_por_venta_entry = tk.Entry(self)
        self.ingresos_por_venta_entry.place(relx=0.05, rely=0.1)

        self.label_costos_por_venta = tk.Label(self, text="Costos por venta:")
        self.label_costos_por_venta.place(relx=0.05, rely=0.2)

        self.costos_por_venta_entry = tk.Entry(self)
        self.costos_por_venta_entry.place(relx=0.05, rely=0.25)

        self.label_remuneracion_obrero = tk.Label(self, text="Costos de remuneración por obrero:")
        self.label_remuneracion_obrero.place(relx=0.05, rely=0.35)

        self.remuneracion_obrero_entry = tk.Entry(self)
        self.remuneracion_obrero_entry.place(relx=0.05, rely=0.4)

        # Labels y entries de día desde y día hasta (derecha arriba)
        self.label_dia_desde = tk.Label(self, text="Desde qué día:")
        self.label_dia_desde.place(relx=0.75, rely=0.05)

        self.rango_desde_entry = tk.Entry(self)
        self.rango_desde_entry.place(relx=0.75, rely=0.1)

        self.label_dia_hasta = tk.Label(self, text="Hasta qué día:")
        self.label_dia_hasta.place(relx=0.75, rely=0.15)

        self.rango_hasta_entry = tk.Entry(self)
        self.rango_hasta_entry.place(relx=0.75, rely=0.20)
        

        # Labels y entries de obreros (medio arriba)
        self.label_frecuencia = tk.Label(self, text="Cantidad de veces que se ausentaron los obreros:")
        self.label_frecuencia.place(relx=0.4, rely=0.05)
        
        self.label_frecuencia_obrero_cero = tk.Label(self, text = "0 obreros")
        self.label_frecuencia_obrero_cero.place(relx = 0.4, rely=0.1)
        
        self.frecuencia_obrero_cero_entry = tk.Entry(self)
        self.frecuencia_obrero_cero_entry.place(relx = 0.47, rely=0.1)
        
        self.label_frecuencia_obrero_uno = tk.Label(self, text = "1 obrero")
        self.label_frecuencia_obrero_uno.place(relx = 0.4, rely=0.15)
        
        self.frecuencia_obrero_uno_entry = tk.Entry(self)
        self.frecuencia_obrero_uno_entry.place(relx = 0.47, rely=0.15)
        
        self.label_frecuencia_obrero_dos = tk.Label(self, text = "2 obreros")
        self.label_frecuencia_obrero_dos.place(relx = 0.4, rely=0.2)
        
        self.frecuencia_obrero_dos_entry = tk.Entry(self)
        self.frecuencia_obrero_dos_entry.place(relx = 0.47, rely=0.2)
        
        self.label_frecuencia_obrero_tres = tk.Label(self, text = "3 obreros")
        self.label_frecuencia_obrero_tres.place(relx = 0.4, rely=0.25)
        
        self.frecuencia_obrero_tres_entry = tk.Entry(self)
        self.frecuencia_obrero_tres_entry.place(relx = 0.47, rely=0.25)
        
        self.label_frecuencia_obrero_cuatro = tk.Label(self, text = "4 obreros")
        self.label_frecuencia_obrero_cuatro.place(relx = 0.4, rely=0.3)
        
        self.frecuencia_obrero_cuatro_entry = tk.Entry(self)
        self.frecuencia_obrero_cuatro_entry.place(relx = 0.47, rely=0.3)
        
        self.label_frecuencia_obrero_cinco = tk.Label(self, text = "5 o más obreros")
        self.label_frecuencia_obrero_cinco.place(relx = 0.4, rely=0.35)
        
        self.frecuencia_obrero_cinco_entry = tk.Entry(self)
        self.frecuencia_obrero_cinco_entry.place(relx = 0.47, rely=0.35)
        
        self.ok_button = tk.Button(self, text="OK", command=lambda: mostrar_datos(self, dias, obreros), width=20)
        self.ok_button.place(relx=0.45, rely=0.5)
        
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
        
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=scrollbar.set)

        def mostrar_datos(self, dias, obreros):
            try:
                rango_desde = int(self.rango_desde_entry.get())
                rango_hasta = int(self.rango_hasta_entry.get())
                ingresos_venta = float(self.ingresos_por_venta_entry.get())
                costos_venta = float(self.costos_por_venta_entry.get())
                remuneracion_obrero = float(self.remuneracion_obrero_entry.get())
                
                frecuencias = [self.frecuencia_obrero_cero_entry.get(),
                               self.frecuencia_obrero_uno_entry.get(),
                               self.frecuencia_obrero_dos_entry.get(),
                               self.frecuencia_obrero_tres_entry.get(),
                               self.frecuencia_obrero_cuatro_entry.get(),
                               self.frecuencia_obrero_cinco_entry.get(),]
                
                if rango_hasta < rango_desde or rango_desde > dias or rango_desde < 0 or rango_hasta > dias:
                    messagebox.showerror("Error", "Rango invalido")
                    
                if ingresos_venta < 0 or costos_venta < 0 or remuneracion_obrero < 0:
                    messagebox.showerror("Error", "No se pueden ingresar valores negativos")
                
                lista_frecuencias = list(map(int, frecuencias))
                
                for i in lista_frecuencias:
                    if i <= 0:
                        messagebox.showerror("Error", "Las frecuencias deben ser positivas y enteras")
                
                objeto_parametros = Parametros(ingresos_venta = ingresos_venta, 
                                               costo_venta = costos_venta, 
                                               remuneracion_obrero = remuneracion_obrero)
                
                objeto_parametros.setear_probabilidades(lista_frecuencias)
                
                self.treeview.delete(*self.treeview.get_children())  # Limpiar la tabla
                
                lista = simulacion(dias, obreros, rango_desde, rango_hasta, objeto_parametros)
                
                for i, obj in enumerate(lista, start=0):
                    self.treeview.insert("", "end", text=str(i), values=(
                        obj.get_dia(), obj.get_rnd_obrero(), obj.get_obreros_ausentes(), obj.get_obreros_presentes(), 
                        obj.get_planta_operable(), '$' + str(obj.get_beneficio()), '$' + str(obj.get_beneficio_acumulado())))
                    
                self.label_beneficio_total = tk.Label(self, text=f"Beneficio total: ${lista[-1].get_beneficio_acumulado()}")
                self.label_beneficio_total.place(relx=0.45, rely=0.9)
                
            except ValueError:
                messagebox.showerror("Error", "Ingreso inválido")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trabajo Práctico N.º3")
        self.geometry("400x300")

        self.generate_button = tk.Button(self, text="Comenzar", command=self.open_main_window, width=15, height=2)
        self.generate_button.place(relx=0.5, rely=0.5, anchor="center")

    def open_main_window(self):
        MainWindow(self)
