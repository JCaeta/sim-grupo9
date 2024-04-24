import matplotlib.pyplot as plt

def histograma(numeros, intervalos):
    frecuencias, bins, _ = plt.hist(numeros, bins=intervalos, edgecolor='white')

    for freq, intervalo in zip(frecuencias, bins[:-1]):
        plt.text(intervalo + (bins[1] - bins[0]) / 2, freq, str(int(freq)), ha='center', va='bottom')

    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de números aleatorios')
    plt.show()
