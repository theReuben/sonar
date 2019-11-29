from __future__ import division
import networkx as nx 
from cascade_models.independent_cascade_model import independent_cascade_model
from working_cascade_models import random_seed
from tqdm import tqdm as tqdm

def graph_of_expectation(G, iterations=1000, seed=None):
	"""
	The graph of expectation is an undirected graph,
	which is a subgraph of the passed graph G,
	where the nodes in the graph are present if the proportion
	of times they are in the final propogation exceed the threshold
	value theta.
	The graph_of_expectation method returns the Tau of the 
	graph of expectation, which is a dictionary of the number of times
	each node is present in the propagation, given the initial seed.
	"""
	if (seed == None):
		seed = G.nodes()
	tau = {}
	# Initialise each tau to 0
	for v in G.nodes():
		tau[v] = 0
	# Record the tau for each node over all iterations
	for i in range(iterations):
		covered = independent_cascade_model(G, seed)
		for u in covered:
			tau[u] += 1
	return tau
