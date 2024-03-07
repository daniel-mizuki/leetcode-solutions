"""
Solution for Valid Anagram
"""

from collections import Counter


class Solution:
    """
    Solution for Valid Anagram
    """

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
