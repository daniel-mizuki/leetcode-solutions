"""Tests for Invert Binary Tree problem"""

import pytest
from leetcode_solutions.invert_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_invert_tree(root, expected):
    tree_node = TreeNode.from_list(root)
    tree_node = Solution().invertTree(tree_node)
    tree_list = tree_node.to_list() if tree_node else []
    assert tree_list == expected
