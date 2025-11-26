import numpy as np
from funcoes_suporte import floadFill, geraDesenho

# Gerando a matriz aleatória:
n = int(input('Digite o valor de n que deseja para a matriz de dimensões n X n: '))
matriz = np.random.randint(0, 2, (n, n))
print(f'Matriz inicial:')
print(matriz)

# Chamando a função floadFill:
listaDePiscinas = floadFill(matriz=matriz)

# Alterando os valores de cada piscina:
novoValor = 2
for piscina in listaDePiscinas:
    for coordenada in piscina:
        matriz[coordenada[0]][coordenada[1]] = novoValor
    novoValor += 1
print(f'\nMatriz com piscinas preenchidas:')
print(matriz)

# Criando o desenho:
geraDesenho(matriz=matriz)