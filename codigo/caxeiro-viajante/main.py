import math
import random
from pathlib import Path
#esclarendo bases
#baseA --->  eil51.tsp
#baseB -->  

CAMINHO_BASE = Path(__file__).parent / "bases"

baseA = CAMINHO_BASE/"eil51.tsp"
baseB = CAMINHO_BASE/"gr666.tsp"
baseC = CAMINHO_BASE/"pcb3038.tsp"
baseD = CAMINHO_BASE/"u159.tsp"
baseE = CAMINHO_BASE/"ulysses16.tsp"

def gravarCidades(arquivoCidade):
    lendoArquivo = False
    listaCidades = []
    with open (arquivoCidade, "r") as arquivo:
        for linha in arquivo:
            if linha == "NODE_COORD_SECTION\n":
                lendoArquivo = True
                print("Leitura inicializada!")
                pass

            elif linha == "EOF\n":
                print("Leitura finalizada!")
                break
            
            elif lendoArquivo == True:
                linha = linha.split()
                cidade1 = (int(linha[0]), float(linha[1]), float(linha[2]))
                listaCidades.append(cidade1)

        return listaCidades

def calcularDistancia(cidade1, cidade2): #fitness
    x1 = cidade1[1]
    x2 = cidade2[1]

    y1 = cidade1[2]
    y2 = cidade2[2]

    dx = x1 - x2
    dy = y1 - y2

    distancia = (math.sqrt(dx**2 + dy**2) ) + 0.5
    return int(distancia)

def calcularFitness(rota):
        fit = 0
        
        for j in range(len(rota) - 1):
            f = calcularDistancia(rota[j], rota[j+1])
            fit += f

        #somando o ultima da lista com o primeiro (volta ao ponto inicial)
        f = calcularDistancia(rota[0], rota[-1])
        fit += f

        return fit

    
def calcularRotas(listaCidades):
    populacaoRotas = []
    populacaoFitness = []

    #repete o processo 100 vezes para criar 100 rotas diferentes    
    for i in range(100):
        #embaralha a listacidades criando uma rota automaticamente
        rota = listaCidades.copy()
        random.shuffle(rota)

        fit = calcularFitness(rota)
        populacaoRotas.append(rota)
        populacaoFitness.append(fit)

    return populacaoRotas, populacaoFitness

def melhoresRotas(populacaoRotas, populacaoFitness):
    elite = []
    #ordena as listas em ordem crescente com base no fitness, e rota é organizado junto para não perder a conexão c/ os indices
    ordFitRotas = sorted(zip(populacaoFitness, populacaoRotas))

    elite = ordFitRotas[:10]

    return elite

def torneio(populacaoRotas,populacaoFitness):

    #sorteia 3 posicoes aletorias da populacao rotas
    posicoes = random.sample(range(len(populacaoRotas)), 3)

    posicaofit = posicoes[0]
    #associa o primeira posicao sorteada ao fit (as duas listas são interligadas pelos indices)
    menorFit = populacaoFitness[posicoes[0]]
    for f in posicoes:
        if populacaoFitness[f] < menorFit:
            menorFit = populacaoFitness[f]
            posicaofit = f

    return populacaoRotas[posicaofit]

def crossover(rota):
    cidades = random.sample(range(len(rota)), 5)
    return cidades

def gerarFilho(populacaoRotas, populacaoFitness):
    rotaPai = torneio(populacaoRotas, populacaoFitness)
    rotaMae = torneio(populacaoRotas, populacaoFitness)

    genePai = crossover(rotaPai)

    filho = []
    filho.append(rotaPai[genePai[0]])
    filho.append(rotaPai[genePai[1]])
    filho.append(rotaPai[genePai[2]])

    for cidade in rotaMae:
        if cidade not in filho:
            filho.append(cidade)

    return filho

# def main(base):
#     while escolha != 0:
#     print("Escolha uma base: ")
#     listaCidades = gravarCidades()




listaCidadesA = gravarCidades(baseA)
populacaoA, fitnessA = calcularRotas(listaCidadesA)
eliteBaseA = melhoresRotas(populacaoA, fitnessA)

print(eliteBaseA[0][0])


