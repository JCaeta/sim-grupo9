import tkinter as tk
from tkinter import ttk, messagebox
from logica import simulacion


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
                self.destroy()
                SimulacionWindow(self.master, dias, obreros)
            else:
                messagebox.showerror("Error", "La cantidad de días de la simulación tiene que estar entre 1 y 100.000")
        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")


class SimulacionWindow(tk.Toplevel):
    def __init__(self, parent, dias, obreros):
        super().__init__(parent)
        self.title("Simulación")
        self.geometry("1450x400")

        self.label_dia_desde = tk.Label(self, text="Ingrese desde que día de la simulación quiere observar: ")
        self.label_dia_desde.pack()

        self.rango_desde_entry = tk.Entry(self)
        self.rango_desde_entry.pack()

        self.label_dia_hasta = tk.Label(self, text="Ingrese hasta que día de la simulación quiere observar: ")
        self.label_dia_hasta.pack()

        self.rango_hasta_entry = tk.Entry(self)
        self.rango_hasta_entry.pack()

        self.ok_button = tk.Button(self, text="OK", command=lambda: mostrar_datos(self, dias, obreros))
        self.ok_button.pack()

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
        self.treeview.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=scrollbar.set)

        def mostrar_datos(self, dias, obreros):
            try:
                rango_desde = int(self.rango_desde_entry.get())
                rango_hasta = int(self.rango_hasta_entry.get())

                if rango_hasta < rango_desde or rango_desde > dias or rango_desde < 0 or rango_hasta > dias:
                    messagebox.showerror("Error", "Rango invalido")
                else:
                    self.treeview.delete(*self.treeview.get_children())  # Limpiar la tabla
                    lista = simulacion(dias, obreros, rango_desde, rango_hasta)
                    for i, obj in enumerate(lista, start=0):
                        self.treeview.insert("", "end", text=str(i), values=(
                            obj.dia, obj.rnd_obrero, obj.obreros_ausentes, obj.obreros_presentes, obj.planta_operable,
                            '$' + str(obj.beneficio), '$' + str(obj.beneficio_acumulado)))

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
