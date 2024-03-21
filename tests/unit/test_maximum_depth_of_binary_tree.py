"""Tests for Maximum Depth of Binary Tree solution"""

import pytest

from leetcode_solutions.maximum_depth_of_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
    ],
)
def test_maximum_depth_of_binary_tree(root, expected):
    assert Solution().maxDepth(TreeNode.from_list(root)) == expected
