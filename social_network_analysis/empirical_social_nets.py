import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=',')
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=',')

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    print("Average degree: %.2f" % np.mean(list(dict(G.degree()).values())))
def plot_degree_distribution(G):
    plt.hist(list(dict(G.degree()).values()), histtype = 'step')
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

# basic_net_stats(G1)
# basic_net_stats(G2)
# plot_degree_distribution(G1)
# plot_degree_distribution(G2)
# plt.savefig("village_hist.pdf")

gen1 = (G1.subgraph(c).copy() for c in nx.connected_components(G1))
gen2 = (G2.subgraph(c).copy() for c in nx.connected_components(G2))
G1_LCC = max(gen1, key=len) #largest connected component
G2_LCC = max(gen2, key=len)
print(G1_LCC.number_of_nodes()/G1.number_of_nodes())
print(G2_LCC.number_of_nodes()/G2.number_of_nodes())

plt.figure()
nx.draw(G1_LCC,  node_color="red", edge_color="blue", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC,  node_color="red", edge_color="blue", node_size=20)
plt.savefig("village2.pdf")
