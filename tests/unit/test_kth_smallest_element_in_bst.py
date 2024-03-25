"""
Tests for Kth Smallest Element in a BST problem
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

import pytest

from leetcode_solutions.kth_smallest_element_in_bst import Solution, TreeNode


@pytest.mark.parametrize(
    "root, k, expected",
    [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        ([], 1, None),
        ([1, 2, 3], 5, None),
        ([1, 2, 3], 0, None),
        ([1, 2, 3], -1, None),
        ([1, None, 2, None, None, None, 3], 3, 3),
        ([7, 3, 8, 1, 5, None, None, None, 2, 4, 6], 4, 4),
    ],
)
def test_kth_smallest(root, k, expected):
    """
    Test kth smallest
    """
    assert Solution().kthSmallest(TreeNode.from_list(root), k) == expected
