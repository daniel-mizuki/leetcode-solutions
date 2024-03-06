"""
Unit tests for Dijkstra's algorithm
"""

import pytest
from leetcode_solutions.dijkstras import Solution


def example_1():
    """
    Example 1
    """
    n = 5
    edges = [
        [0, 1, 10],
        [0, 2, 3],
        [1, 3, 2],
        [2, 1, 4],
        [2, 3, 8],
        [2, 4, 2],
        [3, 4, 5],
    ]
    src = 0
    solution = {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}

    return n, edges, src, solution


def example_2():
    """
    Example 2
    """
    n = 2
    edges = [[0, 1, 5]]
    src = 0
    solution = {0: 0, 1: 5}

    return n, edges, src, solution


def example_3():
    """
    Example 3
    """
    n = 4
    edges = [[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]]
    src = 1
    solution = {0: -1, 1: 0, 2: 2, 3: 6}

    return n, edges, src, solution


def example_4():
    """
    Example 4
    """
    n = 5
    edges = [
        [0, 1, 10],
        [0, 2, 3],
        [1, 3, 2],
        [2, 1, 4],
        [2, 3, 8],
        [2, 4, 2],
        [3, 4, 5],
    ]
    src = 4
    solution = {0: -1, 1: -1, 2: -1, 3: -1, 4: 0}

    return n, edges, src, solution


@pytest.mark.parametrize(
    "n, edges, src, solution", [example_1(), example_2(), example_3(), example_4()]
)
def test_shortest_path(n, edges, src, solution):
    """
    Test Dijkstra's algorithm
    """
    assert Solution().shortestPath(n, edges, src) == solution
