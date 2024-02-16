"""
Dynamic array data structure
"""


class DynamicArray:
    """
    Dynamic array data structure
    """

    def __init__(self, capacity: int):
        """
        Initializes the dynamic array with a specific capacity.

        Args:
            capacity (int): Capacity of the dynamic array
        Raises:
            ValueError: Capacity must be greater than 0
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def get(self, i: int) -> int:
        """
        Returns the element at index i.

        Args:
            i (int): Index of the element
        Returns:
            int: Element at index i
        Raises:
            IndexError: Index out of bounds
        """
        if not self._isIndexInBounds(i):
            raise IndexError("Index out of bounds")
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        """
        Sets the element at index i to n.

        Args:
            i (int): Index of the element
            n (int): New value of the element
        Raises:
            IndexError: Index out of bounds
        """
        if not self._isIndexInBounds(i):
            raise IndexError("Index out of bounds")
        self._array[i] = n

    def pushback(self, n: int) -> None:
        """
        Pushes the element n to the end of the array.

        Args:
            n (int): New element
        """
        if self._isFull():
            self.resize()
        self._array[self._size] = n
        self._size += 1

    def popback(self) -> int:
        """
        Pops and returns the element at the end of the array.

        Returns:
            int: Element at the end of the array
        Raises:
            IndexError: Array is empty
        """
        if self._size == 0:
            raise IndexError("Array is empty")
        self._size -= 1
        return self._array[self._size]

    def resize(self) -> None:
        """
        Doubles the capacity of the array.
        """
        new_capacity = self._capacity * 2
        self._array = [
            self._array[i] if i < self._size else None for i in range(new_capacity)
        ]
        self._capacity = new_capacity

    def getSize(self) -> int:
        """
        Returns the number of elements in the array.

        Returns:
            int: Number of elements in the array
        """
        return self._size

    def getCapacity(self) -> int:
        """
        Returns the capacity of the array.

        Returns:
            int: Capacity of the array
        """
        return self._capacity

    def _isIndexInBounds(self, i: int) -> bool:
        return 0 <= i < self._size

    def _isFull(self) -> bool:
        return self._size == self._capacity
