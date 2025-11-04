import funcoes_suporte as fs
import matplotlib.pyplot as plt
import numpy as np

# Perguntando ao usuário a dimensão da matriz quadrada que deseja gerar:
n = int(input("\n\nDigite um inteiro n para gerar uma matriz n X n que representará o labirinto: "))

# Gerando a matriz:
matrizGerada = fs.geraMatriz(n=n)

# Mostrando a matriz e as coordenadas de início e fim:
print('\n\n Matriz gerada aleatoriamente:\n')
print(matrizGerada[0])
print(f'\nCoordenadas do início: {matrizGerada[1]}')
print(f'Coordenadas do final: {matrizGerada[2]}')

# Chamando a função para resolver o menor caminho:
resultado = fs.AEstrela(matriz=matrizGerada[0], inicio=matrizGerada[1], fim=matrizGerada[2])

# Visualização dos resultados:
print('\n\n\n**********   Resultados   **********')
if resultado is None:
    print('\n\nSem solução! Não existe caminho entre os pontos do labirinto!\n\n\n')
else:
    resultado.insert(0, matrizGerada[1])
    print('\n\nMenor caminho (em coordenadas):\n')
    print(resultado)
    matriz = matrizGerada[0].astype(object)
    matriz[matrizGerada[1][0]][matrizGerada[1][1]] = 'S'
    matriz[matrizGerada[2][0]][matrizGerada[2][1]] = 'E'
    destaques = resultado
    plt.imshow(matrizGerada[0], cmap='Blues', interpolation='nearest')
    for i in range(matrizGerada[0].shape[0]):
        for j in range(matrizGerada[0].shape[1]):
            cor_texto = 'red' if (i, j) in destaques else 'black'
            plt.text(j, i, f'{matriz[i, j]}',
                    ha='center', va='center',
                    color=cor_texto, fontsize=12, fontweight='bold')

    plt.xticks(np.arange(matrizGerada[0].shape[1]))
    plt.yticks(np.arange(matrizGerada[0].shape[0]))
    plt.grid(False)
    plt.show()
