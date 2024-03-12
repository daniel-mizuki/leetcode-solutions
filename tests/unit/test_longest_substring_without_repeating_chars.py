"""
Tests for Longest Substring Without Repeating Characters solution
"""

import pytest

from leetcode_solutions.longest_substring_without_repeating_chars import Solution


@pytest.mark.parametrize(
    "s, solution",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        ("", 0),
        ("abcxyzxabcdefghijklmnopqrstuvw", 26),
    ],
)
def test_longest_substring_without_repeating_chars(s, solution):
    """
    Test Longest Substring Without Repeating Characters
    """
    assert Solution().lengthOfLongestSubstring(s) == solution
