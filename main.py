import math
#esclarendo bases
#baseA --->  eil51.tsp
#baseB -->  

baseA = "eil51.tsp"
baseB = "gr666.tsp"
baseC = "pcb3038.tsp"
baseD = "u159.tsp"
baseE = "ulysses16.tsp"

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
                cidade1 = (linha[0], linha[1], linha[2])
                listaCidades.append(cidade1)

        return listaCidades

    def calcularDistancia(cidade1, cidade2):
        x1 = cidade1[1]
        x2 = cidade2[1]

        y1 = cidade1[2]
        y2 = cidade2[2]

        dx = x1 - x2
        dy = y1 - y2

        distancia = (math.sqrt(dx**2 + dy**2) ) + 0.5
        return int(distancia)

        

listaCidades = gravarCidades(baseA)

for cidade in listaCidades:
    print(cidade)



