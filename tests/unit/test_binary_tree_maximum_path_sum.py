"""
Tests for Binary Tree Maximum Path Sum problem
"""

import pytest
from leetcode_solutions.binary_tree_maximum_path_sum import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode.from_list([1, 2, 3]), 6),
        (TreeNode.from_list([-10, 9, 20, None, None, 15, 7]), 42),
        (TreeNode.from_list([-3]), -3),
    ],
)
def test_binary_tree_maximum_path_sum(root, expected):
    """
    Test binary tree maximum path sum
    """
    assert Solution().maxPathSum(root) == expected
