"""
Solution for Longest Consecutive Sequence problem
"""

from typing import List


class Solution:
    """
    Solution for Longest Consecutive Sequence problem
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of
        the longest consecutive elements sequence.

        Args:
            nums (List[int]): List of integers
        Returns:
            int: Length of the longest consecutive elements sequence
        """

        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 in num_set:
                continue

            curr_len = 1
            while num + curr_len in num_set:
                curr_len += 1

            max_len = max(max_len, curr_len)

        return max_len
