from graph_utils import *;
from vsa import vsa


def main():
    graph = random_graph(20, 0.1)
    np_graph = graph_to_numpy(graph)
    vertices = vsa(np_graph)
    write_to_file('out.svg', graph, vertices)
    print(vertices)


if __name__ == '__main__':
    main()
