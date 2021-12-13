from igraph import Graph
from typing import Tuple, List
from abc import ABC,abstractmethod


class ChessGraphGenerator(ABC):
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m

    def _is_position_valid(self, dx, dy, x, y):
        if dx + x < 0 or dy + y < 0 or dx + x >= self.n or dy + y >= self.m or (dx == 0 and dy == 0):
            return False
        return True

    @abstractmethod
    def _get_possible_moves(self) -> Tuple[List[int], List[int]]:
        pass

    @abstractmethod
    def _get_neighbors(self, x, y) -> List[Tuple[int, int]]:
        pass

    def _coordinate_to_index(self, x, y):
        return y * self.m + x

    def get_edges(self):
        total_edges: List[Tuple[int, int]] = []
        for i in range(self.n):
            for j in range(self.m):
                index = self._coordinate_to_index(i, j)
                neighbors = self._get_neighbors(i, j)
                total_edges += [(index, self._coordinate_to_index(x, y)) for x, y in neighbors]
        total_edges = [(source, target) for (source, target) in total_edges if source < target]
        return total_edges


class KingGraph(ChessGraphGenerator):

    def _get_possible_moves(self) -> Tuple[List[int], List[int]]:
        move_x = [-1, 0, 1]
        move_y = [-1, 0, 1]
        return move_x, move_y

    def _get_neighbors(self, x, y) -> List[Tuple[int, int]]:
        move_x, move_y = self._get_possible_moves()
        neighbors = [(x + dx, y + dy) for dx in move_x for dy in move_y if self._is_position_valid(dx, dy, x, y)]
        return neighbors


class RookGraph(ChessGraphGenerator):

    def _get_possible_moves(self) -> Tuple[List[int], List[int]]:
        move_x = list(range(-1 * self.n + 1, 0)) + list(range(0, self.n))
        move_y = list(range(-1 * self.m + 1, 0)) + list(range(0, self.m))
        return move_x, move_y

    def _get_neighbors(self, x, y) -> List[Tuple[int, int]]:
        move_x, move_y = self._get_possible_moves()
        neighbors = [(x + dx, y) for dx in move_x if self._is_position_valid(dx, 0, x, y)]
        neighbors += [(x, y + dy) for dy in move_y if self._is_position_valid(0, dy, x, y)]
        return neighbors


def rook_graph(n: int, m: int):
    helper = RookGraph(n, m)
    edges = helper.get_edges()
    graph = Graph(n * m, edges=edges, directed=False)
    return graph


def king_graph(n: int, m: int):
    helper = KingGraph(n, m)
    edges = helper.get_edges()
    graph = Graph(n * m, edges=edges)
    return graph
