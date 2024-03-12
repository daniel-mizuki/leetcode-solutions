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

        max_len = 0
        substr_start = 0
        seen = {}

        for i, char in enumerate(s):
            if char in seen and seen[char] >= substr_start:
                substr_start = seen[char] + 1
            elif (curr_len := i - substr_start + 1) > max_len:
                max_len = curr_len

            seen[char] = i

        return max_len

        # max_len = 0
        # substr_start = 0
        # seen = set()

        # for i, char in enumerate(s):
        #     while char in seen:
        #         seen.remove(s[substr_start])
        #         substr_start += 1

        #     if (curr_len := i - substr_start + 1) > max_len:
        #         max_len = curr_len

        #     seen.add(char)

        # return max_len
