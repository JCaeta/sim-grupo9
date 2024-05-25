import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("TP Nº4 - SIMULACIÓN - 4K3 - UTN FRC - GRUPO 9")
root.geometry("1000x320")
root.configure(bg="#f3f3d1")

icon = tk.PhotoImage(file='utn.png')
root.iconphoto(False, icon)


# IZQUIERDA DE LA VENTANA #
label_cantidad_tiempo = tk.Label(root, text="Cantidad de tiempo (X)", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_cantidad_tiempo.place(x=20, y=20)
entry_cantidad_tiempo = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_cantidad_tiempo.place(x=65, y=50)

label_minuto_desde = tk.Label(root, text="Minuto desde (i)", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_minuto_desde.place(x=50, y=80)
entry_minuto_desde = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_desde.place(x=65, y=110)

label_minuto_hasta = tk.Label(root, text="Minuto hasta (j)", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_minuto_hasta.place(x=50, y=140)
entry_minuto_hasta = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_hasta.place(x=65, y=170)

# MEDIO DE LA VENTANA #
label_evento_llegada_empleado = tk.Label(root, text="Evento llegada_empleado", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_evento_llegada_empleado.place(x=300, y=20)
entry_media_evento_llegada_empleado = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_media_evento_llegada_empleado.place(x=350, y=50)
label_media_llegada_empleado = tk.Label(root, text="Media", font=("Helvetica", 12), bg='#f3f3d1')
label_media_llegada_empleado.place(x=460, y=50)

label_evento_llegada_tecnico = tk.Label(root, text="Evento llegada_tecnico", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_evento_llegada_tecnico.place(x=300, y=110)
label_hora_A_llegada_tecnico = tk.Label(root, text="A (en horas)", font=("Helvetica", 12), bg='#f3f3d1')
label_hora_A_llegada_tecnico.place(x=460, y=140)
entry_hora_A_llegada_tecnico = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_hora_A_llegada_tecnico.place(x=350, y=140)
label_minuto_B_llegada_tecnico = tk.Label(root, text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
label_minuto_B_llegada_tecnico.place(x=460, y=170)
entry_minuto_B_llegada_tecnico = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_B_llegada_tecnico.place(x=350, y=170)

# DERECHO DE LA VENTANA #
label_evento_fin_registro_huella = tk.Label(root, text="Evento fin_registro_huella", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_evento_fin_registro_huella.place(x=600, y=20)
entry_minuto_A_fin_registro_huella = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_A_fin_registro_huella.place(x=650, y=50)
label_minuto_A_fin_registro_huella = tk.Label(root, text="A (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
label_minuto_A_fin_registro_huella.place(x=750, y=50)
entry_minuto_B_fin_registro_huella = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_B_fin_registro_huella.place(x=650, y=80)
label_minuto_B_fin_registro_huella = tk.Label(root, text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
label_minuto_B_fin_registro_huella.place(x=750, y=80)

label_evento_fin_registro_huella = tk.Label(root, text="Evento fin_mantenimiento_terminal", font=("Helvetica", 14, "bold"), bg='#f3f3d1')
label_evento_fin_registro_huella.place(x=600, y=110)
entry_minuto_A_fin_registro_huella = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_A_fin_registro_huella.place(x=650, y=140)
label_minuto_A_fin_registro_huella = tk.Label(root, text="A (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
label_minuto_A_fin_registro_huella.place(x=750, y=140)
entry_minuto_B_fin_registro_huella = tk.Entry(root, font=("Helvetica", 12), width=10)
entry_minuto_B_fin_registro_huella.place(x=650, y=170)
label_minuto_B_fin_registro_huella = tk.Label(root, text="B (en minutos)", font=("Helvetica", 12), bg='#f3f3d1')
label_minuto_B_fin_registro_huella.place(x=750, y=170)


# Botón
button = tk.Button(root, text="Generar simulación", font=("Consolas", 16, "bold"), bg="lightblue", fg="black")
button.place(x=360, y=250, width=300, height=50)

# Iniciar el bucle principal de la interfaz
root.mainloop()
