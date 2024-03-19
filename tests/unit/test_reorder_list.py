"""Tests for Reorder List solution"""

import pytest

from leetcode_solutions.reorder_list import Solution, ListNode

example_1 = (
    ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
    ListNode(1, ListNode(4, ListNode(2, ListNode(3)))),
)

example_2 = (
    ListNode(1, ListNode(2)),
    ListNode(1, ListNode(2)),
)

example_3 = (
    ListNode(1),
    ListNode(1),
)

example_4 = (
    None,
    None,
)

example_5 = (
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
    ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3))))),
)


@pytest.mark.parametrize(
    "head, expected",
    [example_1, example_2, example_3, example_4, example_5],
)
def test_reorder_list(head, expected):
    """
    Test Reorder List
    """
    Solution().reorderList(head)
    assert head == expected
