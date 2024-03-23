"""
Solution for Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from typing import List, Optional

from .util.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = []
        queue = [root]

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            levels.append(level)

        return levels
