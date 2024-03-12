"""
Solution for Longest Substring Without Repeating Characters problem
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    """
    Solution for Longest Substring Without Repeating Characters problem
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, returns the length of the longest substring
        without repeating characters.

        Args:
            s (str): String to check

        Returns:
            int: Length of the longest substring
        """

        seen = {}
        max_len = 0
        substr_start = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= substr_start:
                substr_start = seen[char] + 1
            else:
                max_len = max(max_len, i - substr_start + 1)

            seen[char] = i

        return max_len
