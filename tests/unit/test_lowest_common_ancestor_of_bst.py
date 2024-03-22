"""
Test for Lowest Common Ancestor of a Binary Search Tree problem
"""

import pytest

from leetcode_solutions.lowest_common_ancestor_of_bst import Solution, TreeNode


@pytest.mark.parametrize(
    "root, p, q, expected",
    [
        (
            TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            TreeNode(2),
            TreeNode(8),
            TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
        ),
        (
            TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            TreeNode(2),
            TreeNode(4),
            TreeNode.from_list([2, 0, 4, None, None, 3, 5]),
        ),
        (
            TreeNode.from_list([2, 1]),
            TreeNode(2),
            TreeNode(1),
            TreeNode.from_list([2, 1]),
        ),
    ],
)
def test_lowest_common_ancestor(root, p, q, expected):
    """
    Test lowest common ancestor
    """
    assert Solution().lowestCommonAncestor(root, p, q) == expected
