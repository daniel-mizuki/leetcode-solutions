"""
Dijkstra's algorithm
"""

from typing import Dict


class Solution:
    """
    Dijkstra's algorithm solution
    """

    @staticmethod
    def shortestPath(n: int, edges: list[list[int]], src: int) -> Dict[int, int]:
        """
        Given a weighted, directed graph, and a starting vertex, return
        the shortest distance from the starting vertex to every vertex
        in the graph.

        Args:
            n (int): The number of vertices in the graph
            edges (list[list[int]]): A list of tuples, each representing
                a directed edge in the form (u, v, w), where u is the
                source vertex, v is the destination vertex, and w is
                the weight of the edge
            src (int): The source vertex from which to start the
                algorithm
        Returns:
            Dict[int, int]: The shortest distance from the starting
                vertex to every vertex in the graph
        """
        unvisted = {v for v in range(n)}
        distances = {v: float("inf") for v in range(n)}

        distances[src] = 0

        while unvisted:
            curr = min(unvisted, key=lambda v: distances[v])
            for edge in [e for e in edges if e[0] == curr and e[1] in unvisted]:
                v = edge[1]
                w = edge[2]
                distances[v] = min(distances[v], distances[curr] + w)

            unvisted.remove(curr)

        return {k: (v if v != float("inf") else -1) for k, v in distances.items()}
