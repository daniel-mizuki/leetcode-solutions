"""
Tests for Subtree of Another Tree problem
"""

import pytest

from leetcode_solutions.subtree_of_another_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, sub_root, expected",
    [
        (
            TreeNode.from_list([3, 4, 5, 1, 2]),
            TreeNode.from_list([4, 1, 2]),
            True,
        ),
        (
            TreeNode.from_list([3, 4, 5, 1, 2, None, None, None, None, 0]),
            TreeNode.from_list([4, 1, 2]),
            False,
        ),
        (
            TreeNode.from_list([1, 2, 3, 4, 5, 6]),
            TreeNode.from_list([1, 2, 3, 4, 5, 6]),
            True,
        ),
        (
            TreeNode.from_list([1, 2, 3, 4, 5, 6]),
            TreeNode.from_list([1, 2, 3, 4, 5, 6, 7]),
            False,
        ),
        (
            TreeNode.from_list([1, 2, 3, 4, 5, 6]),
            TreeNode.from_list([1, 2, 3, 4, 5]),
            False,
        ),
        (
            TreeNode.from_list([1, 1, None, 1, 2]),
            TreeNode.from_list([1, 1, 2]),
            True,
        ),
        (
            TreeNode(1),
            None,
            True,
        ),
        (
            None,
            TreeNode(1),
            False,
        ),
        (
            None,
            None,
            True,
        ),
    ],
)
def test_subtree_of_another_tree(root, sub_root, expected):
    """
    Test subtree of another tree
    """
    assert Solution().isSubtree(root, sub_root) == expected
