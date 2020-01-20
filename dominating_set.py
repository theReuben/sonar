from expectation_digraph import digraph_of_expectation

def dominating_set(G) :
	V = G.nodes
	D = set()
	tmp = set()
	for v in V :
		if len(V - tmp) == 0 :
			break
		D.add(v)
		tmp.add(v)
		[tmp.add(i) for i in G[v]]
	return D