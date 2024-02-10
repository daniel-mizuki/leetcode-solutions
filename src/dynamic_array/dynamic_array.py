class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def get(self, i: int) -> int:
        if not self._isIndexInBounds(i):
            raise IndexError("Index out of bounds")
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        if not self._isIndexInBounds(i):
            raise IndexError("Index out of bounds")
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self._isFull():
            self.resize()
        self._array[self._size] = n
        self._size += 1

    def popback(self) -> int:
        pass

    def resize(self) -> None:
        pass

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity
    
    def _isIndexInBounds(self, i: int) -> bool:
        return 0 <= i < self._size
    
    def _isFull(self) -> bool:
        return self._size == self._capacity
