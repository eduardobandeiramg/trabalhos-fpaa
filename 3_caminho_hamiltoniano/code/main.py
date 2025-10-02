# Substitua abaixo quantos nós deseja no seu grafo:
nos = 5
# Substitua abaixo o quão completo você deseja que seu grafo seja (de 0 a 1, sendo 0 totalmente incompleto e 1 totalmente completo)
completude = 1


##############################################################################
import networkx as nx
import matplotlib.pyplot as plt
import funcoes_suporte as fs

# Gerando o grafo aleatório:
G = nx.gnp_random_graph(nos, completude)

# Implementando o algoritmo:
listaDeNos = list(range(nos))
nosVisitados = []
todosOsCaminhosPossiveis = G.edges
caminhosPercorridos = []
fs.andeParaONo(listaDeNos[0], listaDeNos, nosVisitados, todosOsCaminhosPossiveis, caminhosPercorridos)

# Desenhando o grafo:
#nx.draw(G, with_labels=True, font_weight='bold', font_color="white")
#plt.show()

# Desenhando a solução: