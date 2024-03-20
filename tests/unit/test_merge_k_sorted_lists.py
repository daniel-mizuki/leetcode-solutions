"""
Tets for Merge k Sorted Lists
"""

import pytest

from leetcode_solutions.merge_k_sorted_lists import Solution, ListNode


@pytest.fixture
def linked_lists(request):
    """
    Creates a list of linked lists
    """
    lists = []

    for lst in request.param:
        lists.append(ListNode.from_list(lst))

    return lists


@pytest.mark.parametrize(
    "linked_lists, expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2, 3], [], []], [1, 2, 3]),
    ],
    indirect=["linked_lists"],
)
def test_merge_k_lists(linked_lists, expected):
    """
    Test merge k sorted lists
    """
    assert Solution().mergeKLists(linked_lists) == ListNode.from_list(expected)
