"""
Solution for Search in Rotated Sorted Array problem
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

from typing import List
import bisect


class Solution:
    """Solution for Search in Rotated Sorted Array problem"""

    def search(self, nums: List[int], target: int) -> int:
        """
        Finds the index of a target in a sorted and rotated array.

        Args:
            nums (List[int]): List of integers
            target (int): Target
        Returns:
            int: Index of target
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
