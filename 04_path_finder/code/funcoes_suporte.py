import numpy as np

# Função que gera uma matriz aleatória:
def geraMatriz(n: int):
    matriz = np.random.randint(0, 2, (n,n))
    inicio = (np.random.randint(0,n), np.random.randint(0,n))
    fim = (np.random.randint(0,n), np.random.randint(0,n))
    return (matriz, inicio, fim)

# Função que implementa o algoritmo A*
def AEstrela(matriz, inicio, fim, caminho: list = []):
    print(caminho)
    input()
    posicaoAtual = caminho[len(caminho) - 1] if len(caminho) > 0 else inicio
    if posicaoAtual == fim:
        return caminho
    else:
        possibilidades = [(posicaoAtual[0]-1, posicaoAtual[1]), (posicaoAtual[0]+1, posicaoAtual[1]), (posicaoAtual[0], posicaoAtual[1]-1), (posicaoAtual[0], posicaoAtual[1]+1)]
        possibilidades = [elemento for elemento in possibilidades if (elemento[0] >= 0 and elemento[0] < len(matriz)) and (elemento[1] >= 0 and elemento[1] < len(matriz)) and elemento not in caminho]
        listaMenoresHeuristicas = []
        for caminhoPossivel in possibilidades:
            if matriz[caminhoPossivel[0]][caminhoPossivel[1]] == 0 or caminhoPossivel == fim:
                heuristica = abs(caminhoPossivel[0] - fim[0]) + abs(caminhoPossivel[1] - fim[1])
                listaMenoresHeuristicas.append((caminhoPossivel, heuristica))
        listaMenoresHeuristicas = sorted(listaMenoresHeuristicas, key= lambda x: x[1])
        if len(listaMenoresHeuristicas) > 0:
            for proximoCaminho in range(0, len(listaMenoresHeuristicas) + 1):
                if proximoCaminho == 0:
                    caminho.append(listaMenoresHeuristicas[proximoCaminho][0])
                else:
                    caminho.pop()
                    caminho.append(listaMenoresHeuristicas[proximoCaminho][0])
                return AEstrela(matriz=matriz, inicio=inicio, fim=fim, caminho=caminho)
        return