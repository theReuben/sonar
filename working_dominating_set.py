from __future__ import division
from dominating_set import dominating_set
from expectation_digraph import digraph_of_expectation
from cascade_models.decreasing_cascade_model import decreasing_cascade_model
from cascade_models.independent_cascade_model import independent_cascade_model
from cascade_models.linear_threshold_model import linear_threshold_model
import networkx as nx 

def assign_edge_weights(G):
    for x,y in G.edges() :
        G[x][y]['weight'] = 0.1

def main() :
	G = nx.barabasi_albert_graph(100, 5, None)
	assign_edge_weights(G)
	DG, tau = digraph_of_expectation(G, theta=0.1)
	assign_edge_weights(DG)
	seed = dominating_set(DG)
	print("seed : {0}".format(seed))
	activated = linear_threshold_model(G, seed)
	print("activated : {0}".format(activated))
	print(len(seed))
	print(len(activated)/len(G))


if __name__ == '__main__':
	main()