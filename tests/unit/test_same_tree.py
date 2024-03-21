"""
Tests for Same Tree solution
"""

import pytest

from leetcode_solutions.same_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "p, q, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([1, 2, 3, 4], [1, 2, 3, None, 4], False),
        ([], [], True),
    ],
)
def test_same_tree(p, q, expected):
    """
    Test same tree
    """
    p_tree = TreeNode.from_list(p)
    q_tree = TreeNode.from_list(q)
    assert Solution().isSameTree(p_tree, q_tree) == expected
