from math import cos, pi
import random

def binario_para_real(valor_binario, limite_inferior, limite_superior):
    return limite_inferior + (float(valor_binario) / (pow(2, valor_binario.bit_length()) - 1))*(limite_superior - limite_inferior)

def sphere(x):
    return x**2

def rastrigin(x):
    return 10 + x**2 - 10 * cos(2*pi*x)

def rosenbrock(x1, x2):
    return 100*(x2 - x1**2)**2 + (1 - x1)**2

# Codificando pensando no sphere
# Depois pensar em em generalizações

def gerar_individuo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def gerar_populacao(quantidade, tamanho):
    return [gerar_individuo(tamanho) for _ in range(quantidade)]

def fitness(individuo):
    return sum(individuo)

def selecao_torneio(populacao, tamanho_torneio=2):
    candidatos = random.sample(populacao, tamanho_torneio)
    vencedor = min(candidatos, key=fitness)
    return vencedor.copy()  # Evita modificar o pai original

def crossover(pai1, pai2, taxa_crossover):
    if random.random() < taxa_crossover:
        ponto = random.randint(1, len(pai1) - 1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
    else:
        ponto = None
        filho1 = pai1.copy()
        filho2 = pai2.copy()
    return filho1, filho2, ponto

def mutacao(individuo, taxa_mutacao):
    mutado = individuo.copy()
    for i in range(len(mutado)):
        if random.random() < taxa_mutacao:
            mutado[i] = 1 - mutado[i]
    return mutado

TAMANHO_POPULACAO = 6
TAMANHO_CROMOSSOMO = 10
NUM_GERACOES = 30
TAXA_CROSSOVER = 0.80
TAXA_MUTACAO = 0.01  # Probabilidade por bit
TAMANHO_TORNEIO = 2

def algoritmo_genetico():
    populacao = gerar_populacao(TAMANHO_POPULACAO, TAMANHO_CROMOSSOMO)
    historico_melhor = []
    historico_media = []

    # A geração 0 é a população inicial; a última pode ser NUM_GERACOES.
    for geracao in range(NUM_GERACOES + 1):
        melhor = min(populacao, key=fitness)
        melhor_fitness = fitness(melhor)
        media_fitness = sum(map(fitness, populacao)) / len(populacao)

        historico_melhor.append(melhor_fitness)
        historico_media.append(media_fitness)

        print(f"Geração {geracao:02d} | "
              f"Melhor fitness: {10 - melhor_fitness:2d} | "
              f"Média: {media_fitness:.2f} | "
              f"Melhor indivíduo: {''.join(map(str, melhor))}")

        # Para se encontrou a solução ótima ou atingiu o limite.
        if melhor_fitness == TAMANHO_CROMOSSOMO or geracao == NUM_GERACOES:
            break

        # Elitismo: mantém o melhor indivíduo sem mutação.
        nova_populacao = [melhor.copy()]

        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecao_torneio(populacao, TAMANHO_TORNEIO)
            pai2 = selecao_torneio(populacao, TAMANHO_TORNEIO)

            filho1, filho2, _ = crossover(pai1, pai2, TAXA_CROSSOVER)
            filho1 = mutacao(filho1, TAXA_MUTACAO)
            filho2 = mutacao(filho2, TAXA_MUTACAO)

            nova_populacao.append(filho1)
            if len(nova_populacao) < TAMANHO_POPULACAO:
                nova_populacao.append(filho2)

        populacao = nova_populacao

    melhor_final = min(populacao, key=fitness)
    return melhor_final, historico_melhor, historico_media


melhor, historico_melhor, historico_media = algoritmo_genetico()
print("\nMelhor solução encontrada:", melhor)
print("Aptidão final:", 10-fitness(melhor), "/", TAMANHO_CROMOSSOMO)
