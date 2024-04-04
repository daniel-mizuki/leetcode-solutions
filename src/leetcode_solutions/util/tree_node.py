"""
Tree Node class to be used for LeetCode problems
"""


class TreeNode:
    """
    Tree Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, lst):
        # tree_node_list = []

        # for i, val in enumerate(lst):
        #     tree_node = cls(val) if val is not None else None
        #     tree_node_list.append(tree_node)

        #     if i == 0 or tree_node is None:
        #         continue

        #     parent = tree_node_list[(i - 1) // 2]
        #     if parent is None:
        #         raise ValueError("Invalid tree")
        #     if i % 2 == 0:
        #         parent.right = tree_node
        #     else:
        #         parent.left = tree_node

        # return tree_node_list[0] if tree_node_list else None

        root = None
        node_queue = []

        for i, val in enumerate(lst):
            node = cls(val) if val is not None else None

            if node is not None:
                node_queue.append(node)

            if i == 0:
                root = node
                continue

            parent = node_queue[0]
            if i % 2 == 1:
                parent.left = node
            else:
                parent.right = node
                node_queue.pop(0)

        return root

    def to_list(self):
        lst = list(traverse_level_order_with_none(self))

        while lst and lst[-1] is None:
            lst.pop()

        return lst

    def __eq__(self, other):
        if not other or self.val != other.val:
            return False

        return self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"TreeNode: {self.to_list()}"


def traverse_inorder(tree_node):
    if tree_node.left:
        yield from traverse_inorder(tree_node.left)
    yield tree_node.val
    if tree_node.right:
        yield from traverse_inorder(tree_node.right)


def traverse_preorder(tree_node):
    yield tree_node.val
    if tree_node.left:
        yield from traverse_preorder(tree_node.left)
    if tree_node.right:
        yield from traverse_preorder(tree_node.right)


def traverse_postorder(tree_node):
    if tree_node.left:
        yield from traverse_postorder(tree_node.left)
    if tree_node.right:
        yield from traverse_postorder(tree_node.right)
    yield tree_node.val


def traverse_level_order(tree_node):
    queue = [tree_node]
    while queue:
        node = queue.pop(0)
        yield node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def traverse_level_order_with_none(tree_node):
    queue = [tree_node]
    while queue:
        node = queue.pop(0)
        yield node.val if node else None
        if node:
            queue.append(node.left)
            queue.append(node.right)
