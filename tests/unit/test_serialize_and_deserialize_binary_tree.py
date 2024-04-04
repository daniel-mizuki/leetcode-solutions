"""
Tests for Serialize and Deserialize Binary Tree problem
"""

import pytest
from leetcode_solutions.serialize_and_deserialize_binary_tree import Codec, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode.from_list([1, 2, 3]),
            "[1,2,3]",
        ),
        (
            TreeNode.from_list([-10, 9, 20, None, None, 15, 7]),
            "[-10,9,20,None,None,15,7]",
        ),
        (
            TreeNode.from_list([-3]),
            "[-3]",
        ),
        (
            TreeNode.from_list([]),
            "[]",
        ),
        (
            TreeNode.from_list([1, 2, 3, None, None, 4, 5, 6, 7]),
            "[1,2,3,None,None,4,5,6,7]",
        ),
    ],
)
def test_serialize_and_deserialize_binary_tree(root, expected):
    """
    Test serialize and deserialize binary tree
    """
    ser = Codec()
    deser = Codec()
    assert ser.serialize(root) == expected
    assert deser.deserialize(expected) == root
