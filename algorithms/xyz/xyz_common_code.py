import scipy.sparse as sp
import scipy
import numpy as np


def get_z_vector(sparse: sp.spmatrix, vertex_degree_vector) -> np.ndarray:
    # take rank and decrease by 1, unless rank is already 0
    degree_minus_1_vector = np.select([vertex_degree_vector > 0, vertex_degree_vector == 0],
                                      [vertex_degree_vector - 1,
                                       vertex_degree_vector])
    # 4 5 0 0 7 ... 3 4 0 0 6
    temp_x_vector = get_x_vector(degree_minus_1_vector)
    z_vector = (temp_x_vector * sparse) + 1
    return z_vector


def get_y_vector(sparse: sp.spmatrix, x_vector: np.ndarray):
    return (x_vector * sparse) + x_vector


def get_x_vector(vertex_degree_vector: np.ndarray):
    return vertex_degree_vector / (vertex_degree_vector + 1)
