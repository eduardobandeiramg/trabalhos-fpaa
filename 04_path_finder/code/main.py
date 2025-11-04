import funcoes_suporte as fs

# Perguntando ao usuário a dimensão da matriz quadrada que deseja gerar:
n = int(input("\n\nDigite um inteiro n para gerar uma matriz nxn que representará o labirinto: "))

# Gerando a matriz:
matrizGerada = fs.geraMatriz(n=n)

# Mostrando a matriz e as coordenadas de início e fim:
print('\n\n Matriz gerada aleatoriamente:')
print(matrizGerada[0])
print(f'\nCoordenadas do início: {matrizGerada[1]}')
print(f'Coordenadas do final: {matrizGerada[2]}')

# Chamando a função para resolver o menor caminho:
resultado = fs.AEstrela(matriz=matrizGerada[0], inicio=matrizGerada[1], fim=matrizGerada[2])
print(f'\nResultado:')
print(resultado)

#print("\033[31mTexto vermelho\033[0m")