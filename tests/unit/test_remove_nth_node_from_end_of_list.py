"""
Tests for Remove Nth Node From End of List solution
"""

import pytest
from leetcode_solutions.remove_nth_node_from_end_of_list import Solution, ListNode

example_1 = (
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
    2,
    ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
)

example_2 = (
    ListNode(1),
    1,
    None,
)

example_3 = (
    ListNode(1, ListNode(2)),
    1,
    ListNode(1),
)

example_4 = (
    None,
    1,
    None,
)

example_5 = (
    ListNode(1, ListNode(2)),
    2,
    ListNode(2),
)

example_6 = (
    ListNode(1, ListNode(2)),
    3,
    ListNode(1, ListNode(2)),
)


@pytest.mark.parametrize(
    "head, n, expected",
    [example_1, example_2, example_3, example_4, example_5],
)
def test_remove_nth_node_from_end_of_list(head, n, expected):
    """
    Test Remove Nth Node From End of List
    """
    assert Solution().removeNthFromEnd(head, n) == expected
