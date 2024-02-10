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

def test_dynamic_array_set_out_of_bounds():
    array = DynamicArray(5)
    array.pushback(5)
    array.pushback(6)
    array.pushback(7)
    with pytest.raises(IndexError):
        array.set(3, 8)

def test_dynamic_array_popback():
    array = DynamicArray(5)
    array.pushback(5)
    array.pushback(6)
    array.pushback(7)
    assert array.popback() == 7
    assert array.popback() == 6
    assert array.popback() == 5
    assert array.getSize() == 0
    assert array.getCapacity() == 5
    with pytest.raises(IndexError):
        array.popback()

def test_dynamic_array_resize():
    array = DynamicArray(5)
    array.pushback(5)
    array.pushback(6)
    array.pushback(7)
    array.resize()
    assert array.getCapacity() == 10
    assert array.get(0) == 5
    assert array.get(1) == 6
    assert array.get(2) == 7
    assert array.getSize() == 3

def test_dynamic_array_pushback_with_resize():
    array = DynamicArray(5)
    array.pushback(5)
    array.pushback(6)
    array.pushback(7)
    array.pushback(8)
    array.pushback(9)
    array.pushback(10)
    assert array.getCapacity() == 10
    assert array.get(0) == 5
    assert array.get(1) == 6
    assert array.get(2) == 7
    assert array.get(3) == 8
    assert array.get(4) == 9
    assert array.get(5) == 10
    assert array.getSize() == 6