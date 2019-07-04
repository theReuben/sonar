from __future__ import division
from expectation_graph import graph_of_expectation
import networkx as nx 

def digraph_of_expectation(G, theta=0.05, iterations=1000, seed=None):
	if (seed == None):
		seed = G.nodes()
	tau = {}
	for v in seed:
		seed_v = {v}
		exp = graph_of_expectation(G=G, iterations=iterations, seed=seed_v)
		remove = []
		print("\nNode {0}".format(v))		
		for i in exp:
			exp[i] /= iterations
			if exp[i] < theta or exp[i] == 1.0:
				remove.append(i)
		for rem in remove:
			del exp[rem]
		tau[v] = exp
		print(exp)
	return tau
