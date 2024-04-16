"""
Test for trie data structure
"""

import pytest

from leetcode_solutions.util.trie import Trie


@pytest.mark.parametrize(
    "actions, strings, expecteds",
    [
        (
            ["insert", "search", "search", "startsWith", "insert", "search"],
            ["apple", "apple", "app", "app", "app", "app"],
            [None, True, False, True, None, True],
        ),
        (
            ["insert", "search", "startsWith"],
            ["a", "a", "a"],
            [None, True, True],
        ),
        (
            ["insert", "search", "startsWith"],
            ["a", "b", "b"],
            [None, False, False],
        ),
        (
            ["insert", "search", "insert", "search", "startWith"],
            ["a", "b", "b", "b", "b"],
            [None, False, None, True, True],
        ),
    ],
)
def test_trie(actions, strings, expecteds):
    """
    Test trie
    """
    trie = Trie()
    for action, string, expected in zip(actions, strings, expecteds):
        if action == "insert":
            trie.insert(string)
        elif action == "search":
            assert trie.search(string) == expected
        elif action == "startsWith":
            assert trie.startsWith(string) == expected
