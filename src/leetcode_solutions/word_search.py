"""
Solution for Word Search problem
"""

from collections import defaultdict
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Checks if string is valid based on board

        Args:
            board (List[List[str]]): Board
            word (str): String to check

        Returns:
            bool: True if valid, False otherwise
        """

        n_rows, n_cols = len(board), len(board[0])

        if len(word) > n_rows * n_cols:
            return False

        letter_count = defaultdict(int)
        for row in board:
            for letter in row:
                letter_count[letter] += 1

        for letter in word:
            if letter_count[letter] == 0:
                return False
            letter_count[letter] -= 1

        def helper(row, col, word_idx):
            if word_idx >= len(word):
                return True

            if (
                0 <= row < n_rows
                and 0 <= col < n_cols
                and board[row][col] == word[word_idx]
            ):
                letter = board[row][col]
                board[row][col] = None

                is_word_found = (
                    helper(row - 1, col, word_idx + 1)
                    or helper(row + 1, col, word_idx + 1)
                    or helper(row, col - 1, word_idx + 1)
                    or helper(row, col + 1, word_idx + 1)
                )

                board[row][col] = letter

                return is_word_found

            return False

        for row in range(n_rows):
            for col in range(n_cols):
                if helper(row, col, 0):
                    return True

        return False
