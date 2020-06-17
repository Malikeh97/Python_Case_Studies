import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

N = 20
p = 0.2

def er_graph(N, p):
    """Generate an ER Graph."""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                    G.add_edge(node1, node2)
    return G
G  = er_graph(N, p)
nx.draw(G, with_labels=True, node_color="pink", edge_color="lightblue")
plt.savefig("er_graph.pdf")
