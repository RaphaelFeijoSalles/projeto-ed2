import numpy as np
import matplotlib.pyplot as plt
from funcoes import sphere, binario_para_real


def mostrar_grafico(melhor):
    x = np.linspace(-5, 5, 300)
    y = sphere(x)

    x_inteiros = np.arange(-5, 6)
    y_inteiros = sphere(x_inteiros)

    x_encontrado = binario_para_real(melhor, -5, 5)
    y_encontrado = sphere(x_encontrado)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color="blue", label="f(x) = x²")
    plt.scatter(x_inteiros, y_inteiros, color="gray", alpha=0.6, label="Valores inteiros")
    plt.scatter(0, 0, color="red", s=80, label="Ótimo (0, 0)")
    plt.scatter(x_encontrado, y_encontrado, color="green", s=80, label="Melhor do AG")

    plt.title("Minimização de Função Quadrática com AG")
    plt.xlabel("Valor de x")
    plt.ylabel("Fitness f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
