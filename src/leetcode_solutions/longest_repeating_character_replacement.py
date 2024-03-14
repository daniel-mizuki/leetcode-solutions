"""
Solution for Longest Repeating Character Replacement problem
https://leetcode.com/problems/longest-repeating-character-replacement/
"""

from collections import defaultdict


class Solution:
    """
    Solution for Longest Repeating Character Replacement problem
    """

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, return the length of the
        longest substring containing the same letter you can get after
        replacing at most k characters.

        Args:
            s (str): String to check
            k (int): Maximum number of replacements

        Returns:
            int: Length of the longest substring
        """

        char_freq = defaultdict(int)
        max_freq = 0
        substr_len = 0

        for i, char in enumerate(s):
            char_freq[char] += 1
            max_freq = max(max_freq, char_freq[char])
            if substr_len - max_freq + 1 > k:
                char_freq[s[i - substr_len]] -= 1
            else:
                substr_len += 1

        return substr_len
