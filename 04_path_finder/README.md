o que garante que nao vou voltar em um ponto ja passado?

mostrar resultados exatamente como esperado (lista de coordenadas)

# Algoritmo A*
O algoritmo A* (lê-se "A estrela") é um mecanismo para determinação do menor caminho entre dois pontos de um plano, seja ele um grafo ou uma matriz.

Ele se assemelha muito ao algoritmo de backtracking, com o diferencial de "caminhar" pelo plano priorizando alguma condição/verificação pré-estabelecida, ao invés de fazer isso de forma aleatória. Esse comportamento tenta diminuir o tempo necessário para encontrar o menor caminho, mesmo que essa possibilidade não seja garantida e nem que o caminho encontrado seja, de fato, o menor possível.

## A solução implementada
Neste projeto específico, é gerada uma matriz n X n aleatória utilizando a biblioteca [numpy](https://numpy.org), sendo o n definido pelo usuário no momento da execução do código. Uma vez gerada a matriz, ela é mostrada no console juntamente com os pontos inicial e final, definidos também de forma aleatória através da mesma biblioteca.

---> imagem do input aqui

A matriz gerada é, então passada para a função 'AEstrela()' juntamente aos pontos inicial e final. Essa função recursiva percorre a matriz, escolhendo o próximo ponto do caminho que respeite às seguintes exigências:
* deve estar dentro dos limites da matriz
* deve ser igual a zero (0)
* deve conter a menor distância para o ponto final, dentre as outras opções possíveis (distância = distância vertical + distância horizontal)

Caso haja uma solução, a função retorna o caminho percorrido (ordem das coordenadas dos pontos percorridos). Caso contrário, retorna nulo ('None').

O algoritmo (main.py) que chama as duas funções citadas, então, desenha a matriz gerada com a biblioteca [matplotlib](https://matplotlib.org), destacando os pontos inicial e final e o caminho percorrido, se existir.

## Como executar o código