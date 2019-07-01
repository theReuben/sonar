from __future__ import division
import networkx as nx 

def decreasing_cascade_model2(G, nodes, contagious_nodes, attempted_nodes, active_nodes) :

    class Node :
        number = None
        S = set()
        adj = set()

        def __init__(number) :
            number = number
            S = set()

        def attempted(node) :
            S.add(node)

        def S_size():
            return len(S)

    def decreasing_cascade_model_activation(con, adj) :
        if len(nodes[adj].S) == 0 :
            score = G[con][adj]['weight']
        else :
            score = G[con][adj]['weight'] / len(nodes[adj].S)
        nodes[adj].S.add(con)
        return score

    next_contagious = set()
    this_attempt = set()
    next_active = set()

    if len(nodes) == 0 :
        for n in G.nodes() :
            nodes[n] = Node(n)

        return decreasing_cascade_model2(G, nodes, contagious_nodes, attempted_nodes, active_nodes)


    if len(attempted_nodes) == len(nodes) :        # If all nodes have been attempted, break
        if len(active_nodes) == len(G) :
            print ("All nodes have been activated.")
            print ("{}/{} nodes have been activated.".format(len(active_nodes), len (G)))
        else :
            print("All nodes have been attempted.")
            print ("{}/{} nodes have been activated.".format(len(active_nodes), len (G)))
        return active_nodes
    elif len(contagious_nodes) == 0 :               # If no nodes have been activated in the previous turn, break
        print ("There are no longer any contagious nodes.")
        print ("{}/{} nodes have been activated.".format(len(active_nodes), len (G)))
        return active_nodes
    else :
        for con in contagious_nodes :
            adjacent = set(G[con])
            for adj in adjacent.difference(active_nodes.intersection(adjacent)) :
                this_attempt.add(adj)               # Node has now been attempted
                activate = np.random.uniform()
                if (decreasing_cascade_model_activation(con, adj) > activate) :
                    next_active.add(adj)           # Node has been activated
                    next_contagious.add(adj)        # Node will be contagious at time t+1

        return decreasing_cascade_model2(G, nodes, next_contagious, attempted_nodes.union(this_attempt), active_nodes.union(next_active))

def decreasing_cascade_model(G, seed_set) :
    nodes = {}
    return decreasing_cascade_model2(G, nodes, seed_set, seed_set, seed_set)
