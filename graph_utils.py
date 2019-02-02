from igraph import Graph, ADJ_UNDIRECTED
from igraph.drawing import plot
import numpy as np
import re
import sys

# graph.write('output.graphml', format='graphml')
# layout = graph.layout_grid(width=10, height=10, dim=3)
# graph.write_svg('./out.svg', labels=[str(i) for i in range(n)])


def random_graph(n, p):
    graph: Graph = Graph.Erdos_Renyi(n, p)
    return graph


def random_graph_by_edges(n, e):
    graph: Graph = Graph.Erdos_Renyi(n, m=e)
    return graph


def write_to_graphml(graph: Graph, vertices):
    graph.vs["name"] = [str(i) for i in range(graph.vcount())]
    graph.vs["color"] = [
        'deepskyblue' if i in vertices else 'indianred' for i in range(graph.vcount())]
    graph.write('output.graphml', format='graphml')


def write_to_file(file_name: str, graph: Graph, vertices):
    options = {
        'labels': [str(i) for i in range(graph.vcount())],
        'colors': ['deepskyblue' if i in vertices else 'indianred' for i in range(graph.vcount())],
        'layout': graph.layout_auto()
    }
    graph.write_svg(file_name, height=800, width=800, **options)


def graph_to_numpy(graph: Graph):
    n = graph.vcount()
    a = np.zeros((n, n), dtype=np.byte)
    if len(graph.get_edgelist()) == 0:
        print('got empty graph, no edges')
        sys.exit(-1)
    rows, cols = zip(*graph.get_edgelist())
    a[rows, cols] = 1
    a[cols, rows] = 1
    # a = np.array(graph.get_adjacency().data) --BENCHMARK
    return a


def read_dimacs(filename: str):
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
            if re.search(r'^e (\d*) (\d*).*', line):
                match = re.search(r'^e (\d*) (\d*).*', line)
                source = int(match.group(1))  # dimacs are not 0-index
                dest = int(match.group(2))
                matrix[source - 1, dest - 1] = 1
                matrix[dest - 1, source - 1] = 1
            elif re.search('^c .*', line):
                pass
            elif re.search(r'^p edge (\d*) .*', line):
                match = re.search(r'^p edge (\d*) .*', line)
                vertices_num = int(match.group(1))
                matrix = np.zeros((vertices_num, vertices_num), dtype=np.byte)

    reverse_matrix = np.ones_like(matrix) - matrix

    for i in range(len(reverse_matrix)):
        reverse_matrix[i, i] = 0

    graph = Graph.Adjacency(reverse_matrix.tolist(), mode=ADJ_UNDIRECTED)
    return graph, reverse_matrix
