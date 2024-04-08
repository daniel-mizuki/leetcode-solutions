"""
Tests for Word Search solution
"""

import pytest
from leetcode_solutions.word_search import Solution


@pytest.mark.parametrize(
    "board, word, expected",
    (
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ),
    ),
)
def test_exist(board, word, expected):
    """
    Test exist
    """
    assert Solution().exist(board, word) == expected
