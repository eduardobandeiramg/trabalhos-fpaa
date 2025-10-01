# Digite abaixo quantos nós deseja no seu grafo:
nos = 4

import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo aleatório:
G = nx.gnp_random_graph(nos, 1)

# Acessando arestas:
print(G.edges)

# Desenhando o grafo:
nx.draw(G, with_labels=True, font_weight='bold', font_color="white")
plt.show()

