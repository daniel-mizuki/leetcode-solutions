"""
Tests for String Encode Decode
"""

import pytest
from leetcode_solutions.string_encode_decode import Solution


@pytest.mark.parametrize(
    "strs, solution",
    [
        (["neet", "code", "love", "you"], ["neet", "code", "love", "you"]),
        (["we", "say", ":", "yes"], ["we", "say", ":", "yes"]),
        ([], []),
    ],
)
def test_encode_decode(strs, solution):
    """
    Test String Encode Decode
    """
    assert Solution.decode(Solution.encode(strs)) == solution
