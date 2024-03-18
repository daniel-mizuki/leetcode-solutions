"""
Tests for Reverse Linked List solution
"""

import pytest
from leetcode_solutions.reverse_linked_list import ListNode
from leetcode_solutions.reverse_linked_list import Solution


example_1 = (
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
    ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
)

example_2 = (
    ListNode(1, ListNode(2)),
    ListNode(2, ListNode(1)),
)

example_3 = (
    ListNode(1),
    ListNode(1),
)

example_4 = (
    None,
    None,
)


@pytest.mark.parametrize(
    "head, expected",
    [example_1, example_2, example_3, example_4],
)
def test_reverse_list(head, expected):
    """
    Test Reverse Linked List
    """
    assert Solution().reverseList(head) == expected
