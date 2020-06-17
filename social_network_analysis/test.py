import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

N = 500
p = 0.08

def er_graph(N, p):
    """Generate an ER Graph."""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                    G.add_edge(node1, node2)
    return G

def plot_degree_distribution(G):
    plt.hist(list(dict(G.degree()).values()), histtype = 'step')
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

G1 = er_graph(N, p)
plot_degree_distribution(G1)
G2 = er_graph(N, p)
plot_degree_distribution(G2)
G3 = er_graph(N, p)
plot_degree_distribution(G3)
plt.savefig("hist1.pdf")
# nx.draw(G, with_labels=True, node_color="pink", edge_color="lightblue")
# plt.savefig("er_graph.pdf")
