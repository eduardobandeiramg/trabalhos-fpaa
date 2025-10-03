# Substitua abaixo quantos nós deseja no seu grafo:
nos = 5
# Substitua abaixo o quão completo você deseja que seu grafo seja (de 0 a 1, sendo 0 totalmente incompleto e 1 totalmente completo)
completude = 0.6


##############################################################################
import networkx as nx
import matplotlib.pyplot as plt
import funcoes_suporte as fs

# Gerando o grafo aleatório:
grafo = nx.gnp_random_graph(nos, completude)

# Chamando o método sobre o grafo:
fs.caminhoHamiltoniano(grafo)

# Desenhando o grafo:
nx.draw(grafo, with_labels=True, font_weight='bold', font_color="white")
plt.show()

# Desenhando a solução: