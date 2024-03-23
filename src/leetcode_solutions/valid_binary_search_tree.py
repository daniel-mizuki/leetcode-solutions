"""
Solution for Valid Binary Search Tree problem
https://leetcode.com/problems/valid-binary-search-tree/
"""

from typing import Optional

from .util.tree_node import TreeNode


class Solution:

    def isValidBST(
        self, root: Optional[TreeNode], low=float("-inf"), high=float("inf")
    ) -> bool:
        if root is None:
            return True

        if root.val <= low or root.val >= high:
            return False

        return self.isValidBST(root.left, low, root.val) and self.isValidBST(
            root.right, root.val, high
        )
