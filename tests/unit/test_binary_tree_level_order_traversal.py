"""
Tests for Binary Tree Level Order Traversal solution
"""

import pytest
from leetcode_solutions.binary_tree_level_order_traversal import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, None, 2], [[1], [2]]),
        ([1, 2, 3, 4, 5, 6], [[1], [2, 3], [4, 5, 6]]),
        ([1, 2, 3, None, 5, None, 7], [[1], [2, 3], [5, 7]]),
    ],
)
def test_level_order(root, expected):
    """
    Test level order
    """
    assert Solution().levelOrder(TreeNode.from_list(root)) == expected
