"""
Tests for 3Sum solution
"""

import pytest
from leetcode_solutions.three_sum import Solution


@pytest.mark.parametrize(
    "nums, solution",
    [
        (
            [-1, 0, 1, 2, -1, -4],
            [[-1, -1, 2], [-1, 0, 1]],
        ),
        (
            [0, 1, 1],
            [],
        ),
        (
            [0, 0, 0],
            [[0, 0, 0]],
        ),
        (
            [-1, 0, 1],
            [[-1, 0, 1]],
        ),
        (
            [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        ),
    ],
)
def test_three_sum(nums, solution):
    """
    Test three sum
    """

    assert Solution.threeSum(nums) == solution
