"""
Solution for Binary Tree Maximum Path Sum problem
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

from typing import Optional

from .util.tree_node import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # self.max_sum = float("-inf")

        # def max_gain(node):
        #     if not node:
        #         return 0

        #     left_gain = max(max_gain(node.left), 0)
        #     right_gain = max(max_gain(node.right), 0)
        #     price_newpath = node.val + left_gain + right_gain

        #     self.max_sum = max(self.max_sum, price_newpath)

        #     return node.val + max(left_gain, right_gain)

        # max_gain(root)
        # return self.max_sum
        max_sum = float("-inf")

        def helper(node):
            if node is None:
                return 0

            left_path_sum = max(helper(node.left), 0)
            right_path_sum = max(helper(node.right), 0)

            nonlocal max_sum
            max_sum = max(max_sum, node.val + left_path_sum + right_path_sum)

            return node.val + max(left_path_sum, right_path_sum)

        helper(root)

        return max_sum
