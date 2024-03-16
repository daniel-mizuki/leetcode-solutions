"""
Tests for Find Minimum in Rotated Sorted Array solution
"""

import pytest
from leetcode_solutions.find_minimum_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ],
)
def test_find_minimum_in_rotated_sorted_array(nums, expected):
    """
    Test find minimum in rotated sorted array
    """
    assert Solution().findMin(nums) == expected
