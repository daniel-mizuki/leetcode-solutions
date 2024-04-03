"""
Tests for Create Binary Tree from Preorder and Inorder Traversal
"""

import pytest

from leetcode_solutions.create_bt_from_preorder_and_inorder_traversal import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
        ),
        ([1, 2], [1, 2], TreeNode.from_list([1, None, 2])),
        ([2, 1], [1, 2], TreeNode.from_list([2, 1])),
        # (
        #     [3, 9, 20, 4, 15, 7, 5],
        #     [9, 4, 5, 3, 15, 20, 7],
        #     TreeNode.from_list([3, 9, 20, None, 4, 15, 7, None, None, None, 5]),
        # ),
        ([1], [1], TreeNode.from_list([1])),
        ([], [], None),
    ],
)
def test_build_tree(preorder, inorder, expected):
    """
    Test build tree
    """
    assert Solution().buildTree(preorder, inorder) == expected
