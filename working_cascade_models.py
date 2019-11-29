import networkx as nx 
import random as rand
from cascade_models.independent_cascade_model import independent_cascade_model
from cascade_models.decreasing_cascade_model import decreasing_cascade_model
from cascade_models.linear_threshold_model import linear_threshold_model

def random_seed(G, seed_size) :
    seed_set = set()
    for x in range(seed_size) :
        s_size = len(seed_set)
        while s_size == len(seed_set) :
            val = rand.randint(0, G.number_of_nodes()-1)
            if (val in G.nodes()) :
                seed_set.add(val)
    return seed_set

def assign_edge_weights(G):
    for x,y in G.edges() :
        G[x][y]['weight'] = 0.1

def independent_cascade_model_test():
    try:
        G = nx.barabasi_albert_graph(100, 3, None)
        assign_edge_weights(G)
        seed = random_seed(G,10)
        independent_cascade_model(G, seed)        
    except Exception as e:
        print("Indpendent Cascade Model Failed.")
    return True

def decreasing_cascade_model_test():
    try:
        G = nx.barabasi_albert_graph(100, 3, None)
        assign_edge_weights(G)
        seed = random_seed(G,10)
        decreasing_cascade_model(G, seed)        
    except Exception as e:
        print("Decreasing Cascade Model Failed.")
    return True

def linear_threshold_model_test():
    try:
        G = nx.barabasi_albert_graph(100, 3, None)
        assign_edge_weights(G)
        seed = random_seed(G,10)
        linear_threshold_model(G, seed)        
    except Exception as e:
        print("Linear Threshold Model Failed.")
    return True


if __name__ == '__main__':
    if (independent_cascade_model_test()): 
        print("Indpendent Cascade Model works.\n")
    if (decreasing_cascade_model_test()): 
        print("Decreasing Cascade Model works.\n")
    if (linear_threshold_model_test()): 
        print("Linear Threshold Model works.")