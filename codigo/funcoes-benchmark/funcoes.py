from math import cos, pi


def binario_para_real(bits, limite_inferior, limite_superior):
    decimal = int("".join(str(bit) for bit in bits), 2)
    return limite_inferior + (decimal / (2**len(bits) - 1)) * (limite_superior - limite_inferior)


def sphere(x):
    return x**2


def rastrigin(x):
    return 10 + x**2 - 10 * cos(2*pi*x)


def rosenbrock(x1, x2):
    return 100*(x2 - x1**2)**2 + (1 - x1)**2


def fitness(individuo, funcao="sphere"):
    if funcao == "rosenbrock":
        meio = len(individuo) // 2
        x1 = binario_para_real(individuo[:meio], -2, 2)
        x2 = binario_para_real(individuo[meio:], -2, 2)
        return rosenbrock(x1, x2)

    x = binario_para_real(individuo, -5, 5)
    if funcao == "rastrigin":
        return rastrigin(x)
    return sphere(x)
