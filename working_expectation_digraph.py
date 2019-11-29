from expectation_digraph import digraph_of_expectation
from working_cascade_models import assign_edge_weights
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
	G = nx.barabasi_albert_graph(10, 3, None)
	assign_edge_weights(G)
	DG, tau = digraph_of_expectation(G, theta=0.15)

	nx.draw(DG)
	plt.show()