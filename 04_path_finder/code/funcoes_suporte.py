import numpy as np

# TODO: GERAR MATRIZ COM DENSIDADE MENOR DE OBSTACULOS!!
# Função que gera uma matriz aleatória:
def geraMatriz(n: int):
    matriz = np.random.randint(0, 2, (n,n))
    inicio = (np.random.randint(0,n), np.random.randint(0,n))
    fim = (np.random.randint(0,n), np.random.randint(0,n))
    return (matriz, inicio, fim)

geraMatriz(7)

# Função que implementa o algoritmo A*
def AEstrela(matriz, inicio, fim, caminho):
    posicaoAtual = caminho[len(caminho) - 1]
    if posicaoAtual == fim:
        print('Solução encontrada!')
        return caminho
    else:
        possibilidades = [(posicaoAtual[0]-1, posicaoAtual[1]), (posicaoAtual[0]+1, posicaoAtual[1]), (posicaoAtual[0], posicaoAtual[1]-1), (posicaoAtual[0], posicaoAtual[1]+1)]
        print('possibilidades antes de filtrar:')
        print(possibilidades)
        input()
        possibilidades = [elemento for elemento in possibilidades if (elemento[0] >= 0 and elemento[0] < len(matriz)) and (elemento[1] >= 0 and elemento[1] < len(matriz))]
        print('possibilidades depois de filtrar:')
        print(possibilidades)
        input()
        listaMenoresHeuristicas = []
        for caminhoPossivel in possibilidades:
            if matriz[caminhoPossivel[0]][caminhoPossivel[1]] == 0:
                heuristica = abs(caminhoPossivel[0] - fim[0]) + abs(caminhoPossivel[1] - fim[1])
                listaMenoresHeuristicas.append((caminhoPossivel, ))
                print()
                # TODO: ORDENAR A LISTA DE MENORES HEURISTICAS DE ACORDO COM A HEURISTICA.