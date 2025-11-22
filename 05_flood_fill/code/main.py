import numpy as np
from funcoes_suporte import floadFill, buscaPiscina

# Gerando a matriz aleatória:
n = int(input('Digite o valor de n que deseja para a matriz de dimensões n X n: '))
matriz = np.random.randint(0, 2, (n, n))
print(matriz)

# Chamando a função floadFill:
floadFill(matriz=matriz)