import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def floadFill(matriz):
    listaDePiscinas = []
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            if matriz[linha][coluna] == 0 and (not any((linha,coluna) in sublista for sublista in listaDePiscinas if sublista is not None)):
                resultado = buscaPiscina(pontoAtual=(linha, coluna), matriz=matriz)
                listaDePiscinas.append(resultado)
    return listaDePiscinas


def buscaPiscina(pontoAtual:tuple, matriz, piscina:list = None):
    if piscina is None:
        piscina = []
    piscina.append(pontoAtual)
    pontosPossiveis = [(pontoAtual[0], pontoAtual[1] - 1), (pontoAtual[0], pontoAtual[1] + 1), (pontoAtual[0] - 1, pontoAtual[1]), (pontoAtual[0] + 1, pontoAtual[1])]
    pontosPossiveis = [elemento for elemento in pontosPossiveis if (-1 < elemento[0] < len(matriz)) and ((-1 < elemento[1] < len(matriz))) and elemento not in piscina]
    pontosPossiveis = [elemento for elemento in pontosPossiveis if matriz[elemento[0]][elemento[1]] == 0]
    if not pontosPossiveis:
        return piscina
    for ponto in pontosPossiveis:
        piscina = (buscaPiscina(pontoAtual=ponto, matriz=matriz, piscina=piscina))
    return piscina

def geraDesenho(matriz):
    # obtém o colormap original (hsv) e converte para lista de cores
    base_cmap = plt.cm.get_cmap("hsv", 256)
    colors = base_cmap(np.linspace(0, 1, 256))

    # sobrescreve a cor correspondente ao valor 1 (que vira 0 após o -1)
    colors[0] = [0, 0, 0, 1]  # preto

    # cria um novo colormap com essa alteração
    cmap = ListedColormap(colors)

    plt.imshow(matriz - 1, cmap=cmap)
    plt.axis('off')
    plt.show()