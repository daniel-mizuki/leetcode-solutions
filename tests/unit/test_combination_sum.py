"""
Tests for Combination Sum
"""

import pytest

from leetcode_solutions.combination_sum import Solution


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ],
)
def test_combination_sum(candidates, target, expected):
    """
    Test combination sum
    """
    solution = Solution().combinationSum(candidates, target)
    solution_set = frozenset(tuple(sorted(x)) for x in solution)
    expected_set = frozenset(tuple(sorted(x)) for x in expected)
    assert solution_set == expected_set
