"""
Solution for Create Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/create-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List, Optional

from .util.tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build tree
        """

        # Helper function solution
        inorder_map = {v: i for i, v in enumerate(inorder)}

        preorder_idx = 0

        def build_tree_helper(left=0, right=len(inorder) - 1):
            if left > right:
                return None

            nonlocal preorder_idx
            value = preorder[preorder_idx]
            preorder_idx += 1

            inorder_idx = inorder_map[value]
            node = TreeNode(value)
            node.left = build_tree_helper(left, inorder_idx - 1)
            node.right = build_tree_helper(inorder_idx + 1, right)

            return node

        return build_tree_helper()

        #
        # Recursive solution
        #
        #
        # if not preorder or not inorder:
        #     return None

        # value = preorder.pop(0)
        # root = TreeNode(value)
        # root_index = inorder.index(value)
        # root.left = self.buildTree(preorder, inorder[:root_index])
        # root.right = self.buildTree(preorder, inorder[root_index + 1 :])
        # return root

        #
        # Iterative solution
        #
        #
        # inorder_map = {val: i for i, val in enumerate(inorder)}

        # root = None

        # for val in preorder:
        #     node = TreeNode(val)
        #     node_order = inorder_map[val]

        #     parent = None
        #     curr = root

        #     while curr is not None:
        #         curr_order = inorder_map[curr.val]
        #         temp = curr.left if node_order < curr_order else curr.right
        #         parent, curr = curr, temp

        #     if parent is None:
        #         root = node
        #     elif node_order < inorder_map[parent.val]:
        #         parent.left = node
        #     else:
        #         parent.right = node

        # return root
