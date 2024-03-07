"""
Tests for Top K Frequent Elements solution
"""

import pytest

from leetcode_solutions.top_k_frequent_elements import Solution


@pytest.mark.parametrize(
    "nums, k, solution",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ],
)
def test_top_k_frequent(nums, k, solution):
    """
    Test Top K Frequent Elements
    """
    assert Solution().topKFrequent(nums, k) == solution
