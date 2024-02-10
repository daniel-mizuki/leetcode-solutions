import pytest
from dynamic_array.dynamic_array import DynamicArray

def test_dynamic_array_create():
    array = DynamicArray(5)
    assert array.getCapacity() == 5
    assert array.getSize() == 0

def test_dynamic_array_pushback_and_get():
    array = DynamicArray(5)
    array.pushback(5)
    assert array.getSize() == 1
    assert array.getCapacity() == 5
    assert array.get(0) == 5
    array.pushback(6)
    assert array.getSize() == 2
    assert array.getCapacity() == 5
    assert array.get(0) == 5
    assert array.get(1) == 6
    array.pushback(7)
    assert array.getSize() == 3
    assert array.getCapacity() == 5
    assert array.get(0) == 5
    assert array.get(1) == 6
    assert array.get(2) == 7

def test_dynamic_array_get_out_of_bounds():
    array = DynamicArray(5)
    with pytest.raises(IndexError):
        array.get(5)
    with pytest.raises(IndexError):
        array.get(-1)

def test_dynamic_array_set():
    array = DynamicArray(5)
    array.pushback(5)
    array.pushback(6)
    array.pushback(7)
    array.set(1, 8)
    assert array.get(1) == 8
    assert array.get(0) == 5
    assert array.get(2) == 7
    assert array.getSize() == 3
    assert array.getCapacity() == 5