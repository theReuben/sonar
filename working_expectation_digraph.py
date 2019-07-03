from expectation_digraph import digraph_of_expectation
from working_cascade_models import assign_edge_weights
import networkx as nx

if __name__ == '__main__':
	G = nx.barabasi_albert_graph(100, 3, None)
	assign_edge_weights(G)
	digraph_of_expectation(G)