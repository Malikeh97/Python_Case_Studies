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

basic_net_stats(G1)
basic_net_stats(G2)
plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")
