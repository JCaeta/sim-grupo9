import os
import matplotlib.pyplot as plt


def generar_tabla_frecuencias(numeros, intervalos):
    frecuencias, bins, _ = plt.hist(numeros, bins=intervalos, edgecolor='white')

    # Lista para almacenar los datos de la tabla de distribución de frecuencias
    tabla_datos = []

    for freq, intervalo in zip(frecuencias, bins[:-1]):
        tabla_datos.append({'Intervalo': (intervalo, intervalo + (bins[1] - bins[0])),
                            'Frecuencia Observada': int(freq)})

    # Devolver los datos de la tabla de distribución de frecuencias y el histograma
    return tabla_datos, frecuencias, bins


def generar_histograma(tabla_datos):

    plt.close()
    plt.figure(figsize=(10, 12))

    # Extraer los datos necesarios para el histograma
    intervalos = [dato['Intervalo'] for dato in tabla_datos]
    frecuencias = [dato['Frecuencia Observada'] for dato in tabla_datos]

    # Calcular los límites de las barras del histograma
    limite_inferior = [intervalo[0] for intervalo in intervalos]
    limite_superior = [intervalo[1] for intervalo in intervalos]

    # Calcular los centros de los intervalos para ubicar las barras del histograma
    centros_intervalos = [(lim_inf + lim_sup) / 2 for lim_inf, lim_sup in zip(limite_inferior, limite_superior)]

    # Calcular el ancho de las barras del histograma
    anchura_barras = [(lim_sup - lim_inf) for lim_inf, lim_sup in zip(limite_inferior, limite_superior)]

    # Generar el histograma utilizando plt.bar
    plt.bar(centros_intervalos, frecuencias, width=anchura_barras, edgecolor='white')

    # Agregar etiquetas de frecuencia encima de cada barra
    for centro, freq in zip(centros_intervalos, frecuencias):
        plt.text(centro, freq, str(int(freq)), ha='center', va='bottom')

    etiquetas_intervalos = [f"{lim_inf:.2f} - {lim_sup:.2f}" for lim_inf, lim_sup in
                            zip(limite_inferior, limite_superior)]
    plt.xticks(centros_intervalos, etiquetas_intervalos, rotation=60)

    plt.xlabel('Intervalo')
    plt.ylabel('Frecuencia Observada')
    plt.title('Histograma')

    # Guardar el histograma como imagen
    filename = os.path.join(os.getcwd(), "histograma.png")
    plt.savefig(filename, format='png')

    plt.show()

    return filename
