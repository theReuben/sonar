import networkx as nx

def independent_cascade_model_2(G, contagious_nodes, attempted_nodes, active_nodes) :
    next_contagious = set()                         # Set of nodes going to be passed as contagious at time t+1
    this_attempt = set()                            # Nodes that are going to be attempted at time t
    next_active = set()
    if len(attempted_nodes) == len(G) :        # If all nodes have been attempted, break
        if len(active_nodes) == len(G) :
            print ("All nodes have been activated.")
            print ("{}/{} nodes have been activated.".format(len(active_nodes), len(G)))
        else :
            print("All nodes have been attempted.")
            print ("{}/{} nodes have been activated.".format(len(active_nodes), len(G)))
        return active_nodes
    elif len(contagious_nodes) == 0 :               # If no nodes have been activated in the previous turn, break
        print ("There are no longer any contagious nodes.")
        print ("{}/{} nodes have been activated.".format(len(active_nodes), len(G)))
        return active_nodes
    else :
        for con in contagious_nodes :               # Iterate through contagious nodes
            # Attempt to activate unattempted neighbours
            adjacent = set(G[con])
            for adj in adjacent.difference(active_nodes.intersection(adjacent)):
                this_attempt.add(adj)               # Node has now been attempted
                activate = np.random.uniform()
                if (G[con][adj]['weight'] >= activate) :
                    next_active.add(adj)            # Node has been activated
                    next_contagious.add(adj)        # Node will be contagious at time t+1

        return independent_cascade_model_2(next_contagious, attempted_nodes.union(this_attempt), active_nodes.union(next_active))

def independent_cascade_model(G, seed_set) :
    return independent_cascade_model_2(seed_set, seed_set, seed_set)  # Pass seed set to cascade model
