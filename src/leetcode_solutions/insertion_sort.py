"""
Insertion Sort
"""


class Pair:
    """
    Pair
    """

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __eq__(self, other) -> bool:
        return self.key == other.key and self.value == other.value


class Solution:
    """
    Solution
    """

    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        states = []
        for i, pair in enumerate(pairs):
            j = i - 1
            while j >= 0 and pairs[j].key > pair.key:
                j -= 1
            value = pairs.pop(i)
            pairs.insert(j + 1, value)
            states.append(pairs.copy())

        return states
