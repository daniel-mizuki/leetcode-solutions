"""
Solution for Valid Palindrome problem
https://leetcode.com/problems/valid-palindrome/
"""

import re


class Solution:
    """
    Solution for Valid Palindrome problem
    """

    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, determine if it is a palindrome.

        Args:
            s (str): String to check

        Returns:
            bool: True if it is a palindrome, False otherwise
        """
        s = re.sub("[\\W_]+", "", s).lower()
        return s == s[::-1]
