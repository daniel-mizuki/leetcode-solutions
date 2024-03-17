"""
Tests for Search in Rotated Sorted Array solution
"""

import pytest
from leetcode_solutions.search_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([5, 6, 7, 8, 9, 10], 7, 2),
        ([6, 7, 8, 9, 10, 5], 5, 5),
        ([1, 3], 3, 1),
        ([3, 1], 3, 0),
        ([3, 1], 1, 1),
        ([1], 1, 0),
        ([1], 0, -1),
        ([], 0, -1),
    ],
)
def test_search_in_rotated_sorted_array(nums, target, expected):
    """
    Test search in rotated sorted array
    """
    assert Solution().search(nums, target) == expected
