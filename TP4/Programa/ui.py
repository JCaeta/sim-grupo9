import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trabajo Práctico N.º4 - Sistema de Colas - Grupo 9 - Simulacion - UTN FRC")
        self.geometry("1280x720")
        self.configure(bg="#ffffe6")

        # Label 1: Cantidad de iteraciones
        label1 = tk.Label(self, text="Cantidad de iteraciones", bg="#ffffe6")
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry1 = tk.Entry(self, width=10)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        # Label 2: Hasta qué minuto iterar
        label2 = tk.Label(self, text="Hasta que minuto iterar (en float)", bg="#ffffe6")
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry2 = tk.Entry(self, width=10)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        # Label 3: Evento fin_registro_huella. Ingresar A y B
        label3 = tk.Label(self, text="Evento fin_registro_huella. Ingresar A y B", bg="#ffffe6")
        label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry3a = tk.Entry(self, width=10)
        self.entry3a.grid(row=2, column=1, padx=10, pady=10)
        self.entry3b = tk.Entry(self, width=10)
        self.entry3b.grid(row=2, column=2, padx=10, pady=10)

        # Label 4: Evento llegada_tecnico. Ingresar Hora y +-
        label4 = tk.Label(self, text="Evento llegada_tecnico. Ingresar Hora y +- (hora float, +- float)", bg="#ffffe6")
        label4.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry4a = tk.Entry(self, width=10)
        self.entry4a.grid(row=3, column=1, padx=10, pady=10)
        self.entry4b = tk.Entry(self, width=10)
        self.entry4b.grid(row=3, column=2, padx=10, pady=10)

        # Label 5: Evento fin_mantenimiento_terminal. Ingresar A y B
        label5 = tk.Label(self, text="Evento fin_mantenimiento_terminal. Ingresar A y B", bg="#ffffe6")
        label5.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry5a = tk.Entry(self, width=10)
        self.entry5a.grid(row=4, column=1, padx=10, pady=10)
        self.entry5b = tk.Entry(self, width=10)
        self.entry5b.grid(row=4, column=2, padx=10, pady=10)

        # Label 6: Evento llegada_empleado. Ingresar Media
        label6 = tk.Label(self, text="Evento llegada_empleado. Ingresar Media (float)", bg="#ffffe6")
        label6.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entry6 = tk.Entry(self, width=10)
        self.entry6.grid(row=5, column=1, padx=10, pady=10)

        # Label 7: Ingresar cuántas iteraciones más quiere ver
        label7 = tk.Label(self, text="Ingresar cuántas iteraciones más quiere ver (entera)", bg="#ffffe6")
        label7.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry7 = tk.Entry(self, width=10)
        self.entry7.grid(row=6, column=1, padx=10, pady=10)