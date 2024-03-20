"""
Test for Linked List Cycle problem
"""

import pytest

from leetcode_solutions.linked_list_cycle import Solution, ListNode


@pytest.fixture
def linked_list_cycle(request):
    """
    Creates a linked list with a cycle
    """

    head = curr = ListNode()
    cycle_node = None

    for i, val in enumerate(request.param[0]):
        curr.next = ListNode(val)
        curr = curr.next

        if i == request.param[1]:
            cycle_node = curr

    curr.next = cycle_node

    return head.next


@pytest.mark.parametrize(
    "linked_list_cycle, expected",
    [
        (([3, 2, 0, -4], 1), True),
        (([1, 2], 0), True),
        (([1], 0), True),
        (([1], -1), False),
        (([], 0), False),
    ],
    indirect=["linked_list_cycle"],
)
def test_has_cycle(linked_list_cycle, expected):
    """
    Test has cycle
    """
    assert Solution().hasCycle(linked_list_cycle) == expected
