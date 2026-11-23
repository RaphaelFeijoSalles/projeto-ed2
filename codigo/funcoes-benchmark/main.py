from funcoes import fitness, binario_para_real
from genetico import gerar_populacao, algoritmo_genetico, TAMANHO_POPULACAO, TAMANHO_CROMOSSOMO
from grafico import mostrar_grafico


def mostrar_populacao(nome, populacao):
    print("\n", nome)
    for individuo in populacao:
        bits = "".join(str(bit) for bit in individuo)
        if nome == "Rosenbrock":
            meio = len(individuo) // 2
            x1 = binario_para_real(individuo[:meio], -2, 2)
            x2 = binario_para_real(individuo[meio:], -2, 2)
            print(bits, "| x1 =", round(x1, 4), "| x2 =", round(x2, 4),
                  "| fitness =", round(fitness(individuo, "rosenbrock"), 4))
        else:
            x = binario_para_real(individuo, -5, 5)
            print(bits, "| x =", round(x, 4),
                  "| fitness =", round(fitness(individuo, nome.lower()), 4))


# Sprint 1: cromossomos, populacao inicial e fitness das tres funcoes
populacao = gerar_populacao(TAMANHO_POPULACAO, TAMANHO_CROMOSSOMO)
mostrar_populacao("Sphere", populacao)
mostrar_populacao("Rastrigin", gerar_populacao(TAMANHO_POPULACAO, TAMANHO_CROMOSSOMO))
mostrar_populacao("Rosenbrock", gerar_populacao(TAMANHO_POPULACAO, TAMANHO_CROMOSSOMO * 2))

# O AG completo ainda esta sendo trabalhado para a Sphere
melhor, historico_melhor, historico_media = algoritmo_genetico(populacao)
print("\nMelhor solucao encontrada:", melhor)
print("Aptidao final:", fitness(melhor))
mostrar_grafico(melhor)
