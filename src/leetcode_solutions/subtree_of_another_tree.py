"""
Solution for Subtree of Another Tree problem
"""

from typing import Optional

from .util.tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(node, subnode):
            if node is None:
                return subnode is None
            if subnode is None:
                return subnode is subRoot

            if (
                node.val == subnode.val
                and helper(node.left, subnode.left)
                and helper(node.right, subnode.right)
            ):
                return True

            if (
                node.val == subRoot.val
                and helper(node.left, subRoot.left)
                and helper(node.right, subRoot.right)
            ):
                return True

            return helper(node.left, subRoot) or helper(node.right, subRoot)

        return helper(root, subRoot)

    def isSubtree_alt(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree_alt(root.left, subRoot) or self.isSubtree_alt(
            root.right, subRoot
        )


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
