"""
Solution for Minimum Window Substring problem
https://leetcode.com/problems/minimum-window-substring/
"""

from collections import Counter


class Solution:
    """
    Solution for Minimum Window Substring problem
    """

    def minWindow(self, s: str, t: str) -> str:
        """
        Given a string s and a string t of lengths m and n respectively,
        returns the minimum window substring of s such that every
        character in t (including duplicates) is included in the window.
        If there is no such substring, return the empty string "".

        Args:
            s (str): String which contains minimum window
            t (str): String for which all characters are in the window

        Returns:
            str: Minimum window substring
        """

        start, end = 0, float("inf")

        char_count = Counter(t)
        chars_needed = len(t)

        left_chars = ((i, c) for i, c in enumerate(s) if c in t)
        right_chars = ((i, c) for i, c in enumerate(s) if c in t)

        left, left_char = next(left_chars, (None, None))

        for right, right_char in right_chars:
            char_count[right_char] -= 1
            if char_count[right_char] >= 0:
                chars_needed -= 1

            if chars_needed == 0:
                while char_count[left_char] < 0:
                    char_count[left_char] += 1
                    left, left_char = next(left_chars, (None, None))

                if right - left < end - start:
                    start, end = left, right

                char_count[left_char] += 1
                chars_needed += 1
                left, left_char = next(left_chars, (None, None))

        return s[start : end + 1] if end != float("inf") else ""
