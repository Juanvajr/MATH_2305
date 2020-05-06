import networkx as nx

from functions.weighted_graph_drawings import draw_subtree
from functions.prims_functions import *

G = nx.read_weighted_edgelist('data\G1.txt', nodetype = int)

def prims_algorithm(G, starting_node, show_img = False, show_cost = False):
    
    """Return a minimum spanning tree on an undirected and connected graph 'G'.
    
    Parameters
    ----------
    G : Networkx Graph
        An undirected graphandconnectednetworkx graph 'G'
        
    show_img : bool
        If show_img == True, draw images of the graph and the subtree
        
    algorithm : string
        Then algorithm to use when finding a minimum spanning tree. Valid choices
        are 'kruskal', 'prim', or 'boruvka'. The default is 'kruskal'.
    
    
    Returns
    -------
    G : Networkx Graph
        A minimum spanning weight spanning tree.
        
    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> G.add_edge(0, 3, weight = 2)
    >>> T = nx.minimum_spanning_tree(G)
    >>> sorted(T.edges(data = True))
    [(0, 1, {}), (1, 2, {}), (2, 3, {})]
    """

    if len(G) == 0:
        raise nx.exception.NetworkXPointlessConcept('G has no nodes.')
        
    if starting_node not in G.nodes():
        raise ValueError('Node not found in the graph G')
        
    T = nx.Graph()
    T.add_node(starting_node)
    
    if show_img == True:
        draw_subtree(G, T)
        plt.show()
        
    while T.nodes != G.nodes():
        prims_add_min_cost_edge(G, T)
        if show_img == True:
            draw_subtree(G, T)
            plt.show()
            
    if show_cost == True:
        show_tree_cost(T)
        
    return T

T = prims_algorithm(G, 1, show_img = True, show_cost = True)

    
    
    
    
    
    
    
    
    
    
    
    
    
    

