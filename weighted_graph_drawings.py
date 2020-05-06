import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_weighted_edgelist('data\G1.txt')

def show_weighted_graph(G):
    pos = nx.planar_layout(G)
    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels)
    plt.show()
 
    
def prims_add_min_cost_edge(G, T):
    incident_edges = [
        e
        for e in set(G.edges()) - set(T.edges())
        if any(v in e for v in T.nodes())]
    
    valid_edges = [
        e
        for e in incident_edges
        if[0] not in T.nodes() or e[1] not in T.nodes()]
    
    valid_edges_sorted = sorted(valid_edges, key = lambda x: G.edges()[x]['weight'])
    
    min_e = valid_edges_sorted[0]
    
    T.add_edge(min_e[0], min_e[1], weight = G.edges()[min_e]['weight'])
 
    
    
def draw_subtree(G, T):
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels,)
    nx.draw_networkx_edges(G, pos,
                            edgelist=T.edges(),
                            width=8, alpha=0.5,
                            edge_color='r',)
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=T.nodes(),
                           node_color='r',
                           node_size=500,
                           alpha=0.8)
    plt.show()
    
    
    
    
    
    
    
    
    
