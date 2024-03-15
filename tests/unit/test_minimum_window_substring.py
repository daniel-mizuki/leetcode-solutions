"""
Tests for Minimum Window Substring solution
"""

import pytest
from leetcode_solutions.minimum_window_substring import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("xyzabcdef", "abc", "abc"),  # Entire string t is in s
        ("a", "a", "a"),  # s and t are the same
        ("a", "aa", ""),  # t is longer than s
        ("", "abc", ""),  # s is empty
        ("abc", "", ""),  # t is empty
        ("ABCAAAXYZ", "ZYXA", "AXYZ"),
        ("ABCAAAXYZ", "CAX", "CAAAX"),  # Multiple of same character
        ("AAAABC", "ABC", "ABC"),
        ("ABC", "xy", ""),  # t is not in s
        ("AAAAAAAAAA", "A", "A"),  # t is one character
    ],
)
def test_minimum_window_substring(s, t, expected):
    """
    Test Minimum Window Substring
    """
    assert Solution().minWindow(s, t) == expected
