"""
Test for Longest Consecutive Sequence problem
"""

import pytest
from leetcode_solutions.longest_consecutive_sequence import Solution


@pytest.mark.parametrize(
    "nums, solution",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([-2, -3, -3, 7, -3, 0, 5, 0, -8, -4, -1, 2], 5),
        ([], 0),
    ],
)
def test_longest_consecutive_sequence(nums, solution):
    """
    Test Longest Consecutive Sequence
    """
    assert Solution().longestConsecutive(nums) == solution
