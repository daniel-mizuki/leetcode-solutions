import pytest
from leetcode_solutions.valid_anagram import Solution


@pytest.mark.parametrize(
    "s, t, solution",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "b", False),
        ("ab", "a", False),
    ],
)
def test_is_anagram(s, t, solution):
    assert Solution().isAnagram(s, t) == solution
