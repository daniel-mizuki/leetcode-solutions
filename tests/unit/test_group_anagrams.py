"""
Test for Group Anagrams problem
"""

import pytest

from leetcode_solutions.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs, solution",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            {("bat",), ("nat", "tan"), ("ate", "eat", "tea")},
        ),
        ([""], {("",)}),
        (["a"], {("a",)}),
        (
            ["anagram", "nagaram", "rat", "car"],
            {("car",), ("rat",), ("anagram", "nagaram")},
        ),
    ],
)
def test_group_anagrams(strs, solution):
    """
    Test group anagrams
    """
    solution_set = set(tuple(sorted(x)) for x in Solution.groupAnagrams(strs))
    assert solution_set == solution
