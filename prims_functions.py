
def cost(graph,e):
    return graph.edges()[e]["weight"]


def is_spanning(graph, subgraph):
    return graph.nodes() == subgraph.nodes()

def possible_prims_edges(G, T):
    possible_e = []
    incident_e = []
    for e in set(G.edges()) - set(T.edges()):
        for v in T.nodes():
            if v in e:
                incident_e.append(e)
    for e in incident_e:
        if e[0] not in T.nodes() or e[1] not in T.nodes():
            possible_e.append(e)
    return possible_e





def min_possible_prims_edge(G, T):
    possible_e = possible_prims_edges(G, T)
    min_e = possible_e[0]
    for e in possible_e:
        if cost(G, e) < cost(G, min_e):
            min_e = e
    return min_e












