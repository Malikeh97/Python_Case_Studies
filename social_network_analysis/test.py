import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
nx.draw(G, with_labels = "True", node_color="lightblue", edge_color="grey")
plt.savefig("karate_graph.pdf")
