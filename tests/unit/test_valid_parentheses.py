"""
Tests for Valid Parentheses solution
"""

import pytest
from leetcode_solutions.valid_parentheses import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
    ],
)
def test_valid_parentheses(s, expected):
    """
    Test valid parentheses
    """
    assert Solution().isValid(s) == expected
