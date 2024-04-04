"""
Solution for Serialize and Deserialize Binary Tree problem
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

import ast

from .util.tree_node import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return str(self.tree_to_list(root)).replace(" ", "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.list_to_tree(ast.literal_eval(data))

    def tree_to_list(self, root):
        lst = list(self.level_order_traversal(root))

        while lst and lst[-1] is None:
            lst.pop()

        return lst

    def list_to_tree(self, lst):
        root = None
        node_queue = []

        for i, val in enumerate(lst):
            node = TreeNode(val) if val is not None else None

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

    def level_order_traversal(self, root):
        queue = []

        if root is not None:
            queue.append(root)

        while queue:
            node = queue.pop(0)
            yield node.val if node else None
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
