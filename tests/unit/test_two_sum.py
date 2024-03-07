"""
Test for Two Sum solution
"""

import pytest

from leetcode_solutions.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, solution",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums, target, solution):
    """
    Test two sum
    """
    assert Solution().twoSum(nums, target) == solution
