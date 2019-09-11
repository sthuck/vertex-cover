from igraph import Graph


def remove_clique_3(graph: Graph) -> int:
    cliques = graph.cliques(min=3, max=3)
    to_remove_vertices = set()
    counter = 0

    for clique in cliques:
        if all(graph.vs[vertex].degree() == 2 for vertex in clique):
            counter += 2
            to_remove_vertices = to_remove_vertices.union(clique)

    graph.delete_vertices(to_remove_vertices)
    return counter
