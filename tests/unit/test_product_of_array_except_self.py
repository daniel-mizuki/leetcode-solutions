"""
Test for Product of Array Except Self problem
"""

import pytest

from leetcode_solutions.product_of_array_except_self import Solution


@pytest.mark.parametrize(
    "nums, solution",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_product_except_self(nums, solution):
    """
    Test Product of Array Except Self
    """
    assert Solution().productExceptSelf(nums) == solution
