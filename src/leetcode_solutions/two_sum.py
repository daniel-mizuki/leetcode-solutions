"""
Solution for Two Sum promblem
"""

from typing import List


class Solution:
    """
    Solution for Two Sum promblem
    """

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.

        Args:
            nums (List[int]): List of integers
            target (int): Target
        Returns:
            List[int]: List of indices
        """

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []
