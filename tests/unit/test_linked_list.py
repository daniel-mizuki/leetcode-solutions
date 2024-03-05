import pytest
from leetcode_solutions.linked_list import LinkedList


def test_create_linked_list():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0


def test_insert_head():
    linked_list = LinkedList()
    linked_list.insertHead(1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.size == 1
    linked_list.insertHead(2)
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 1
    assert linked_list.size == 2
    linked_list.insertHead(3)
    assert linked_list.head.value == 3
    assert linked_list.tail.value == 1
    assert linked_list.size == 3


def test_insert_tail():
    linked_list = LinkedList()
    linked_list.insertTail(1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.size == 1
    linked_list.insertTail(2)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2
    assert linked_list.size == 2
    linked_list.insertTail(3)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 3
    assert linked_list.size == 3


def test_get():
    linked_list = LinkedList()
    linked_list.insertTail(1)
    linked_list.insertTail(2)
    linked_list.insertTail(3)
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    assert linked_list.get(3) == -1
    assert linked_list.get(-1) == -1


def test_get_empty():
    linked_list = LinkedList()
    assert linked_list.get(0) == -1


def test_get_values():
    linked_list = LinkedList()
    linked_list.insertTail(1)
    linked_list.insertTail(2)
    linked_list.insertTail(3)
    assert linked_list.getValues() == [1, 2, 3]


def test_get_values_empty():
    linked_list = LinkedList()
    assert linked_list.getValues() == []


def test_remove():
    linked_list = LinkedList()
    linked_list.insertTail(1)
    linked_list.insertTail(2)
    linked_list.insertTail(3)
    linked_list.insertTail(4)
    ret = linked_list.remove(0)
    assert ret
    assert linked_list.getValues() == [2, 3, 4]
    ret = linked_list.remove(1)
    assert ret
    assert linked_list.getValues() == [2, 4]
    ret = linked_list.remove(1)
    assert ret
    assert linked_list.getValues() == [2]
    ret = linked_list.remove(0)
    assert ret
    assert linked_list.getValues() == []
    ret = linked_list.remove(0)
    assert not ret
    assert linked_list.getValues() == []
