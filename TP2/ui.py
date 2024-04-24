import tkinter as tk
from tkinter import ttk, messagebox
from Generador.generador_numeros import *
from Histograma.histograma import *
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage


class MainWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ingreso de muestra e intervalos")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Ingrese el tamaño de la muestra (1-1000000):")
        self.label.pack()

        self.tamaño_entry = tk.Entry(self)
        self.tamaño_entry.pack()

        self.label_intervalos = tk.Label(self, text="Seleccione la cantidad de intervalos:")
        self.label_intervalos.pack()

        self.intervalos_combobox = ttk.Combobox(self, values=[5, 10, 15, 20, 30, 40, 50], state="readonly")
        self.intervalos_combobox.pack()

        self.ok_button = tk.Button(self, text="OK", command=self.validacion_datos)
        self.ok_button.pack()

    def validacion_datos(self):
        try:
            tamaño = int(self.tamaño_entry.get())
            intervalos = int(self.intervalos_combobox.get())
            if 1 <= tamaño <= 1000000:
                self.destroy()
                DistribucionWindow(self.master, tamaño, intervalos)
            else:
                messagebox.showerror("Error", "El tamaño de la muestra tiene que estar entre 1 y 1.000.000")
        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")


class DistribucionWindow(tk.Toplevel):
    def __init__(self, parent, tamaño, intervalos):
        super().__init__(parent)
        self.title("Seleccion de distribución")
        self.geometry("300x150")

        self.label = tk.Label(self, text="Selecciona la distribución:")
        self.label.pack()

        self.distribucion_var = tk.StringVar()
        self.distribucion_var.set("Uniforme")

        self.distribucion_menu = tk.OptionMenu(self, self.distribucion_var, "Uniforme", "Exponencial", "Normal")
        self.distribucion_menu.pack()

        self.ok_button = tk.Button(self, text="OK", command=lambda: self.validacion_datos(tamaño, intervalos))
        self.ok_button.pack()

    def validacion_datos(self, tamaño, intervalos):
        distribucion = self.distribucion_var.get()
        if distribucion == "Uniforme":
            VentanaUniforme(self.master, tamaño, intervalos)
        elif distribucion == "Exponencial":
            VentanaExponencial(self.master, tamaño, intervalos)
        elif distribucion == "Normal":
            VentanaNormal(self.master, tamaño, intervalos)


class VentanaUniforme(tk.Toplevel):
    def __init__(self, parent, tamaño, intervalos):
        super().__init__(parent)
        self.title("Distribución Uniforme")
        self.geometry("300x150")

        self.label_a = tk.Label(self, text="Ingrese el valor de 'a':")
        self.label_a.pack()

        self.a_entry = tk.Entry(self)
        self.a_entry.pack()

        self.label_b = tk.Label(self, text="Ingrese el valor de 'b':")
        self.label_b.pack()

        self.b_entry = tk.Entry(self)
        self.b_entry.pack()

        self.ok_button = tk.Button(self, text="OK", command=lambda: self.validacion_datos(tamaño, intervalos))
        self.ok_button.pack()

    def validacion_datos(self, tamaño, intervalos):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            if b > a:
                nums = [generador_uniforme(a, b) for _ in range(tamaño)]
                self.destroy()
                VentanaNumeros(self.master, nums)
                tabla_datos, _, _ = generar_tabla_frecuencias(nums, intervalos)
                VentanaTablaDistribucionFrecuencia(self.master, tabla_datos)
                img_histograma = generar_histograma(tabla_datos)
                VentanaGuardarExcel(self.master, nums, tabla_datos, img_histograma)
            else:
                messagebox.showerror("Error", "'b' tiene que ser mayor que 'a''.")
        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")


class VentanaExponencial(tk.Toplevel):
    def __init__(self, parent, tamaño, intervalos):
        super().__init__(parent)
        self.title("Distribución exponencial")
        self.geometry("300x150")

        self.label_lambda = tk.Label(self, text="Ingresa el valor de 'lambda':")
        self.label_lambda.pack()

        self.lambda_entry = tk.Entry(self)
        self.lambda_entry.pack()

        self.ok_button = tk.Button(self, text="OK", command=lambda: self.validacion_datos(tamaño, intervalos))
        self.ok_button.pack()

    def validacion_datos(self, tamaño, intervalos):
        try:
            lamda = float(self.lambda_entry.get())
            if lamda > 0:
                nums = [generador_exponencial(lamda) for _ in range(tamaño)]
                self.destroy()
                VentanaNumeros(self.master, nums)
                tabla_datos, _, _ = generar_tabla_frecuencias(nums, intervalos)
                VentanaTablaDistribucionFrecuencia(self.master, tabla_datos)
                img_histograma = generar_histograma(tabla_datos)
                VentanaGuardarExcel(self.master, nums, tabla_datos, img_histograma)
            else:
                messagebox.showerror("Error", "Lambda debe ser positivo")
        except ValueError:
            messagebox.showerror("Error", "Ingreso inválido")


class VentanaNormal(tk.Toplevel):
    def __init__(self, parent, tamaño, intervalos):
        super().__init__(parent)
        self.title("Distribución normal")
        self.geometry("300x150")

        self.label_media = tk.Label(self, text="Ingrese la media:")
        self.label_media.pack()

        self.media_entry = tk.Entry(self)
        self.media_entry.pack()

        self.label_desviacion = tk.Label(self, text="Ingrese la desviación estándar:")
        self.label_desviacion.pack()

        self.desviacion_entry = tk.Entry(self)
        self.desviacion_entry.pack()

        self.ok_button = tk.Button(self, text="OK", command=lambda: self.validacion_datos(tamaño, intervalos))
        self.ok_button.pack()

    def validacion_datos(self, tamaño, intervalos):
        media_input = self.media_entry.get()
        desviacion_input = self.desviacion_entry.get()

        if media_input.strip() == "" or desviacion_input.strip() == "":
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            media = float(media_input)
            desviacion = float(desviacion_input)
            if desviacion >= 0:
                # # Caminos a seguir dependiendo si el tamaño de la muestra es par o impar (Box-Muller)
                nums = []

                # Si el tamaño de la muestra es par
                for _ in range(tamaño // 2):
                    n1, n2 = generador_normal_bm(media, desviacion)
                    nums.extend([n1, n2])

                # Si el tamaño de la muestra es impar
                if tamaño % 2 != 0:
                    nums.append(generador_normal_bm(media, desviacion)[0])  # Se agrega solo el primer numero del par

                self.destroy()
                VentanaNumeros(self.master, nums)
                tabla_datos, _, _ = generar_tabla_frecuencias(nums, intervalos)
                VentanaTablaDistribucionFrecuencia(self.master, tabla_datos)
                img_histograma = generar_histograma(tabla_datos)
                VentanaGuardarExcel(self.master, nums, tabla_datos, img_histograma)
            else:
                messagebox.showerror("Error", "La desviación estándar tiene que ser mayor o igual a 0.")

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")


class VentanaNumeros(tk.Toplevel):
    def __init__(self, parent, numeros):
        super().__init__(parent)
        self.title("Números Aleatorios Generados")
        self.geometry("430x300")

        self.tree = ttk.Treeview(self, columns=("N", "Número"), show="headings")
        self.tree.heading("N", text="N")
        self.tree.heading("Número", text="Número")
        self.tree.pack(fill=tk.BOTH, expand=True, side="left")

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        for i, numero in enumerate(numeros, start=1):
            self.tree.insert("", "end", values=(i, numero))


class VentanaTablaDistribucionFrecuencia(tk.Toplevel):
    def __init__(self, parent, tabla_datos):
        super().__init__(parent)
        self.title("Tabla de Distribución de Frecuencias")
        self.geometry("430x300")

        self.tree = ttk.Treeview(self, columns=("Intervalo", "Frecuencia Observada"), show="headings")
        self.tree.heading("Intervalo", text="Intervalo")
        self.tree.heading("Frecuencia Observada", text="Frecuencia Observada")
        self.tree.pack(fill=tk.BOTH, expand=True, side="left")

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        for dato in tabla_datos:
            int_desde = round((dato['Intervalo'][0]), 2)
            int_hasta = round((dato['Intervalo'][1]), 2)

            intervalo = f"{int_desde:.2f} - {int_hasta:.2f}"
            frecuencia = dato['Frecuencia Observada']

            self.tree.insert("", "end", values=(intervalo, frecuencia))


class VentanaGuardarExcel(tk.Toplevel):
    def __init__(self, parent, numeros, tabla_datos, histograma):
        super().__init__(parent)
        self.title("Guardar en Excel")
        self.geometry("300x100")

        self.label = tk.Label(self, text="¿Desea guardar los datos en Excel?")
        self.label.pack()

        self.save_button = tk.Button(self, text="Guardar", command=lambda: self.guardar_excel(numeros, tabla_datos,
                                                                                              histograma,
                                                                                              'archivo.xlsx'))
        self.save_button.pack()

    def guardar_excel(self, numeros_aleatorios, tabla_datos, histograma, ruta_archivo):
        try:
            # Crear un Excel
            libro = Workbook()
            hoja = libro.active

            # Encabezados para la tabla de números aleatorios
            hoja['B2'] = 'N'
            hoja['C2'] = 'Nº Aleatorio'

            # Columna de números aleatorios en la hoja de Excel
            for i, numero in enumerate(numeros_aleatorios, start=1):
                hoja[f'B{i + 2}'] = i
                hoja[f'C{i + 2}'] = numero

            # Encabezados para la tabla de intervalos y frecuencias
            hoja['E2'] = 'Intervalo'
            hoja['F2'] = 'Fo'  # Frecuencia Observada

            # Escribir los datos de la tabla de intervalos y frecuencias
            for i, dato in enumerate(tabla_datos, start=1):
                int_desde = round(dato['Intervalo'][0], 2)
                int_hasta = round(dato['Intervalo'][1], 2)
                intervalo = f"{int_desde} - {int_hasta}"
                hoja[f'E{i + 2}'] = intervalo
                hoja[f'F{i + 2}'] = dato['Frecuencia Observada']

                # Agregar la imagen del histograma al Excel
            xl_image = XLImage(histograma)
            hoja.add_image(xl_image, 'L2')

            # Guardar el archivo Excel
            libro.save(ruta_archivo)
            messagebox.showinfo(title="Exito", message="Archivo guardado correctamente")
            self.destroy()

        except Exception as e:
            messagebox.showerror(title="Error", message="Tiene el archivo excel abierto. Cierre e intente nuevamente")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trabajo Práctico nº2")
        self.geometry("400x300")

        self.generate_button = tk.Button(self, text="Comenzar", command=self.open_main_window, width=15, height=2)
        self.generate_button.place(relx=0.5, rely=0.5, anchor="center")

    def open_main_window(self):
        MainWindow(self)
