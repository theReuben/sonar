import networkx as nx
import numpy as np

def linear_threshold_model_2(G, contagious_nodes, attempted_nodes, active_nodes, verbose) :

    # Sum of adjacent active node edges
    def sum_adjacent_active(G, node, active_nodes) :
        summ = 0
        for adj in active_nodes.intersection(set(G[node])) :
            summ += G[node][adj]['weight']

        total = 0
        for adj in set(G[node]):
            total += G[node][adj]['weight']

        return (summ > 0.5 * total)

    next_contagious = set()                         # Set of nodes going to be passed as contagious at time t+1
    this_attempt = set()                            # Nodes that are going to be attempted at time t
    next_active = set()
    if len(attempted_nodes) == len(G) :        # If all nodes have been attempted, break
        if len(active_nodes) == len(G) :
            if verbose == True :
                print ("All nodes have been activated.")
                print ("{}/{} nodes have been activated.".format(len(active_nodes), len(G)))
        else :
            if verbose == True :
                print("All nodes have been attempted.")
                print ("{}/{} nodes have been activated.".format(len(active_nodes), len(G)))
        return active_nodes
    elif len(contagious_nodes) == 0 :               # If no nodes have been activated in the previous turn, break
        if verbose == True :
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
                if (G[con][adj]['weight'] >= activate or sum_adjacent_active(G, adj, active_nodes)) :
                    next_active.add(adj)            # Node has been activated
                    next_contagious.add(adj)        # Node will be contagious at time t+1

        return linear_threshold_model_2(G, next_contagious, attempted_nodes.union(this_attempt), active_nodes.union(next_active), verbose)



def linear_threshold_model(G, seed_set, verbose=False) :
    return linear_threshold_model_2(G, seed_set, seed_set, seed_set, verbose=verbose)  # Pass seed set to cascade model
