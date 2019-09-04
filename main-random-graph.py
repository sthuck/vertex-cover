from random_graphs_checks import p0003_graph
from igraph import Graph

def main():
    iterations = 40
    results = []
    for i in range(iterations):
        results.append(p0003_graph())

    sum_components = sum(d['how many components'] for d in results)
    sum_first_component_length = sum([d['component_length_vector'][0] for d in results if len(d['component_length_vector']) > 0])

    print('average number of components:', sum_components/iterations)
    print('average number of vertices in first component:', sum_first_component_length/iterations)


if __name__ == '__main__':
    main()