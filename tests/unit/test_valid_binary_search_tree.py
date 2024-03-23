"""
Test for Valid Binary Search Tree problem
"""

import pytest

from leetcode_solutions.valid_binary_search_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([5, 4, 6, None, None, 3, 7], False),
        ([5, 3, 8, 1, 6, 7, 9], False),
        ([2, 2, 2], False),
        ([2, 2, 2, 2, 2, 2, 2], False),
        ([], True),
        ([1], True),
    ],
)
def test_valid_binary_search_tree(root, expected):
    """
    Test valid binary search tree
    """
    assert Solution().isValidBST(TreeNode.from_list(root)) == expected
