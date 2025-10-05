# Substitua abaixo quantos nós deseja no seu grafo:
nos = 9
# Substitua abaixo o quão denso você deseja que seu grafo seja (de 0 a 1, sendo 0 um grafo nulo e 1 um grafo completo)
densidade = 0.25


##############################################################################
import networkx as nx
import funcoes_suporte as fs

# Gerando o grafo aleatório:
grafo = nx.gnp_random_graph(nos, densidade)

# Chamando o método sobre o grafo:
caminho = fs.caminhoHamiltoniano(grafo)

# Desenhando os grafos:
fs.desenhaGrafos(grafo=grafo, caminho=caminho)