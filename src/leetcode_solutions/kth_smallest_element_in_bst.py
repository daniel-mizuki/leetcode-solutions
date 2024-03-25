"""
Solution for Kth Smallest Element in a BST problem
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

from typing import Optional

from .util.tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or node:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if (k := k - 1) == 0:
                return node.val

            node = node.right

        return None
