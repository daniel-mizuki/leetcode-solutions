import pytest
from leetcode_solutions.insertion_sort import Solution
from leetcode_solutions.insertion_sort import Pair


@pytest.fixture()
def fruit_pairs():
    pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
    return pairs


@pytest.fixture()
def animal_pairs():
    pairs = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]
    return pairs


def test_insertion_sort(fruit_pairs):
    assert Solution().insertionSort(fruit_pairs) == [
        [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")],
        [Pair(2, "banana"), Pair(5, "apple"), Pair(9, "cherry")],
        [Pair(2, "banana"), Pair(5, "apple"), Pair(9, "cherry")],
    ]


def test_insertion_sort_2(animal_pairs):
    assert Solution().insertionSort(animal_pairs) == [
        [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")],
        [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")],
        [Pair(2, "dog"), Pair(3, "cat"), Pair(3, "bird")],
    ]
