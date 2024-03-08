"""
Tests for Valid Palindrome solution
"""

import pytest
from leetcode_solutions.valid_palindrome import Solution


@pytest.mark.parametrize(
    "s, solution",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_valid_palindrome(s, solution):
    """
    Test valid palindrome
    """
    assert Solution().isPalindrome(s) == solution
