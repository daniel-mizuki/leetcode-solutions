import pytest
from leetcode_solutions.linked_list import LinkedList


def test_create_linked_list():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0
