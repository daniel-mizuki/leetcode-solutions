"""
Test for Container With Most Water problem
"""

import pytest

from leetcode_solutions.container_with_most_water import Solution


@pytest.mark.parametrize(
    "heights, solution",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([3, 6], 3),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([0, 0, 0, 0], 0),
        ([-4, -1, -2, -3], 0),
        ([5], 0),
        ([0, -1, -3, 7], 0),
        ([], 0),
    ],
)
def test_container_with_most_water(heights, solution):
    """
    Test Container With Most Water
    """
    assert Solution().maxArea(heights) == solution
