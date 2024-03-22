"""
Solution for Lowest Common Ancestor of a Binary Search Tree problem
"""

from .util.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        # Iterative solution
        low, high = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        node = root

        while node is not None:
            if node.val < low:
                node = node.right
            elif node.val > high:
                node = node.left
            else:
                return node

        return None

        # Recursive solution
        #
        # if root is None:
        #     return None
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)

        # return root

        # More general solution for non-BST binary tree
        #
        # node_data = {
        #     "node": root,
        #     "has_p": False,
        #     "has_q": False,
        #     "children_visited": 0,
        # }
        # stack = [node_data]

        # while stack:
        #     node_data = stack.pop()
        #     node = node_data["node"]

        #     if node_data["has_p"] and node_data["has_q"]:
        #         return node

        #     children_visited = node_data["children_visited"]

        #     if node is None:
        #         if stack:
        #             stack[-1]["children_visited"] += 1

        #     elif children_visited < 2:
        #         if children_visited == 0:
        #             node_data["has_p"] = node_data["has_p"] or node.val == p.val
        #             node_data["has_q"] = node_data["has_q"] or node.val == q.val

        #         child_node = node.left if children_visited == 0 else node.right
        #         child_node_data = {
        #             "node": child_node,
        #             "has_p": False,
        #             "has_q": False,
        #             "children_visited": 0,
        #         }
        #         stack.append(node_data)
        #         stack.append(child_node_data)

        #     elif stack:
        #         stack[-1]["children_visited"] += 1
        #         stack[-1]["has_p"] = stack[-1]["has_p"] or node_data["has_p"]
        #         stack[-1]["has_q"] = stack[-1]["has_q"] or node_data["has_q"]

        # return None
