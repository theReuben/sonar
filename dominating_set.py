from expectation_digraph import digraph_of_expectation

def dominating_set(G) :
	V = G.nodes
	D = set()
	for v in V :
		if V == [G[v] for v in D] :
			break
		D.add(v)
	return D