from expectation_graph import graph_of_expectation
import networkx as nx 

def digraph_of_expectation(G, theta=0.5, iterations=100, seed=None):
	if (seed == None):
		seed = G.nodes()
	tau = {}
	for v in seed:
		seed_v = {v}
		exp = graph_of_expectation(G=G, iterations=iterations, seed=seed_v)
		for i in exp:
			if i < theta:
				del i
		tau[v] = exp

	return tau
