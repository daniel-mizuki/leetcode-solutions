"""
Tests for Merge Two Sorted Lists
"""

import pytest

from leetcode_solutions.merge_two_sorted_lists import Solution
from leetcode_solutions.util.list_node import ListNode


example_1 = (
    ListNode(1, ListNode(2, ListNode(4))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))),
)

example_2 = (
    None,
    ListNode(0),
    ListNode(0),
)

example_3 = (
    ListNode(1),
    ListNode(1),
    ListNode(1, ListNode(1)),
)

example_4 = (
    None,
    None,
    None,
)

example_5 = (
    ListNode(1),
    ListNode(2),
    ListNode(1, ListNode(2)),
)


@pytest.mark.parametrize(
    "list1, list2, expected",
    [example_1, example_2, example_3, example_4],
)
def test_merge_two_sorted_lists(list1, list2, expected):
    """
    Test Merge Two Sorted Lists
    """
    assert Solution().mergeTwoLists(list1, list2) == expected
