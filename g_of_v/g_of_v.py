from igraph import Vertex
import numpy as np


def compute_g_of_v(v: Vertex):
    degree = v.degree()
    if degree == 0:
        return 0

    g_minus = 1/(degree + 1)
    g_plus = np.array([1/(n.degree()*(n.degree() + 1)) for n in v.neighbors()]).sum()
    g = g_plus - g_minus

    return g


def compute_g_of_v_for_testing(v: Vertex):
    degree = v.degree()
    if degree == 0:
        return 0, degree, (0*degree)

    g_minus = 1/(degree + 1)
    g_plus = np.array([1/(n.degree()*(n.degree() + 1)) for n in v.neighbors()]).sum()
    g = g_plus - g_minus
    return g, degree, g*degree

def compute_g_of_v_bwc(v: Vertex):
    degree = v.degree()
    if degree == 0:
        return 0

    g_minus = 1/(degree + 1)
    g_plus = np.array([1/(n.degree()*(n.degree() + 1)) for n in v.neighbors()]).sum()
    g = g_plus - g_minus

    return g