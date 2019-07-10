from __future__ import division
from expectation_graph import graph_of_expectation
from tqdm import tqdm as tqdm
import networkx as nx 

def digraph_of_expectation(G, theta=0.05, iterations=1000, seed=None):
	if (seed == None):
		seed = G.nodes()
	tau = {}
	edge_list = []
	for v in tqdm(seed):
		seed_v = {v}
		exp = graph_of_expectation(G=G, iterations=iterations, seed=seed_v)
		remove = []
		for i in exp:
			exp[i] /= iterations
			if exp[i] < theta or exp[i] == 1.0:
				remove.append(i)
		for rem in remove:
			del exp[rem]
		tau[v] = exp
		for u in tau[v]:
			edge_list.append((v,u))
	DG = nx.DiGraph()
	DG.add_edges_from(edge_list)
	return DG, tau

def cumulative_tau(DG, tau):
	tau_cumulative = {}
	for v in DG.nodes:
		for u in tau:
			# to be completed for gradient/size varying nodes in visualisation
			pass