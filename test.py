import networkx as nx
from functions.weighted_graph_drawings import *
from functions.prims_functions import *
from algorithms.prims import prims_algorithm 

G = nx.read_weighted_edgelist('data\G1.txt', nodetype = int)

T = nx.Graph()

T.add_node(2)



e = min_possible_prims_edge(G, T)
T.add_edge(e[0], e[1], weight = cost(G, e))
draw_subtree(G, T)


e = min_possible_prims_edge(G, T)
T.add_edge(e[0], e[1], weight = cost(G, e))
draw_subtree(G, T)

e = min_possible_prims_edge(G, T)
T.add_edge(e[0], e[1], weight = cost(G, e))
draw_subtree(G, T)


e = min_possible_prims_edge(G, T)
T.add_edge(e[0], e[1], weight = cost(G, e))
draw_subtree(G, T)

e = min_possible_prims_edge(G, T)
T.add_edge(e[0], e[1], weight = cost(G, e))
draw_subtree(G, T)
