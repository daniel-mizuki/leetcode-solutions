"""
Solution for Contains Duplicate
"""


class Solution:
    """
    Solution
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at
        least twice in the array, and return false if every element is
        distinct.

        Args:
            nums (List[int]): List of integers
        Returns:
            bool: True if any value appears at least twice in the array,
                False if every element is distinct
        """
        return len(set(nums)) < len(nums)
