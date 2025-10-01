# Digite abaixo quantos nós deseja no seu grafo:
nos = 4

import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo aleatório:
G = nx.gnp_random_graph(nos, 1)

# Desenhando o grafo:
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()