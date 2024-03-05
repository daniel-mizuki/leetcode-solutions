"""
Linked List
"""


class LinkedListNode:
    """
    Linked List Node
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    """
    Linked List
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Returns the element at index i.

        Args:
            index (int): Index of the element
        Returns:
            int: Element at index i
        """
        if index < 0 or index >= self.size:
            return -1

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node

        return current_node.value

    def insertHead(self, val: int) -> None:
        """
        Inserts a new node at the head of the list
        """
        new_node = LinkedListNode(val, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        """
        Inserts a new node at the tail of the list
        """
        new_node = LinkedListNode(val)
        if self.tail:
            self.tail.next_node = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        """
        Removes the node at index i
        """
        if index < 0 or index >= self.size:
            return False

        previous_node = None
        current_node = self.head
        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next_node

        if not previous_node:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node
        if not current_node.next_node:
            self.tail = previous_node

        del current_node
        self.size -= 1

        return True

    def getValues(self) -> list[int]:
        """
        Returns the values of the list
        """

        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next_node

        return values
