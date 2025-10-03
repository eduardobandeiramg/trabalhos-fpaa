# Substitua abaixo quantos nós deseja no seu grafo:
nos = 7
# Substitua abaixo o quão completo você deseja que seu grafo seja (de 0 a 1, sendo 0 totalmente incompleto e 1 totalmente completo)
completude = 0.85


##############################################################################
import networkx as nx
import funcoes_suporte as fs

# Gerando o grafo aleatório:
grafo = nx.gnp_random_graph(nos, completude)

# Chamando o método sobre o grafo:
caminho = fs.caminhoHamiltoniano(grafo)

# Desenhando os grafos:
fs.desenhaGrafos(grafo=grafo, caminho=caminho)