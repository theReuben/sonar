from __future__ import division
import networkx as nx 
from cascade_models.independent_cascade_model import independent_cascade_model
from working_cascade_models import random_seed

def graph_of_expectation(G, iterations=100, seed=None):
	if (seed == None):
		seed = random_seed(G, int(0.1*len(G)))
	tau = {}
	for v in G.nodes():
		tau[v] = 0
	for i in range(iterations):
		covered = independent_cascade_model(G, seed)
		for u in covered:
			tau[u] += 1
	return tau
