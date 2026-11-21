from math import cos, pi

def binario_para_real(valor_binario, limite_inferior, limite_superior):
    return limite_inferior + valor_binario / pow(2, len(valor_binario)) - 1 (limite_superior - limite_inferior)

def sphere(x):
    return x**2

def rastrigin(x):
    return 10 + x**2 - 10 * cos(2*pi*x)

def rosenbrock(x1, x2):
    return 100*(x2 - x1**2)**2 + (1 - x1)**2

