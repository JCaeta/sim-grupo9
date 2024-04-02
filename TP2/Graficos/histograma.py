import matplotlib.pyplot as plt

def histograma(numeros, intervalos):
    plt.hist(numeros, bins=intervalos, edgecolor='white')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de números aleatorios')
    plt.show()
