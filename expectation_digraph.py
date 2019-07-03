from __future__ import division
from expectation_graph import graph_of_expectation
import networkx as nx 

def digraph_of_expectation(G, theta=0.5, iterations=100, seed=None):
	if (seed == None):
		seed = G.nodes()
	tau = {}
	for v in seed:
		seed_v = {v}
		exp = graph_of_expectation(G=G, iterations=iterations, seed=seed_v)
		remove = []
		for i in exp:
			print(exp[i]/iterations)
			if exp[i]/iterations < theta:
				remove.append(i)
		for rem in remove:
			del exp[rem]
		tau[v] = exp
	return tau
