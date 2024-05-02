from matplotlib import pyplot as plt
import networkx as nx
from random import randint

g = nx.gnp_random_graph(7, 0.3)

for (u, v, w) in g.edges(data = True):
  w['weight'] = randint(1,10)


pos = nx.spring_layout(g)
nx.draw_networkx (g, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes (g, 'weight')
nx.draw_networkx_edge_labels (g, pos, edge_labels=labels)

plt.show()

a_l = [None] * 10
for key, val in g.adjacency():
  a_l[int(key)] = {k: v['weight'] for k,v in val.items()}


print(a_l[0])

