"""
Test cases for Longest Repeating Character Replacement problem
"""

import pytest
from leetcode_solutions.longest_repeating_character_replacement import Solution


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAB", 0, 3),  # No changes allowed, so consider max frequency
        ("BBBBB", 4, 5),  # All characters are the same
        ("ABBBBBB", 2, 7),  # Not all chages are required.
        ("ABCDEFGH", 10, 8),  # Allowed changes is greater than the string length
        ("", 2, 0),  # Empty string
        ("ABCDCECFCGCHI", 6, 11),  # Replace non-adjacent characters
    ],
)
def test_character_replacement(s, k, expected):
    """
    Test Longest Repeating Character Replacement
    """
    assert Solution().characterReplacement(s, k) == expected
