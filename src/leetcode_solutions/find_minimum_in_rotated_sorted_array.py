"""
Solution for Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import List


class Solution:
    """
    Solution for Find Minimum in Rotated Sorted Array problem
    """

    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotatedsorted array.

        Args:
            nums: The sorted and rotated array.

        Returns:
            The minimum element in the array.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            # Check if mid is the min
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # If left side is not sorted, then min is in the left side
            if nums[left] > nums[mid]:
                right = mid - 1
            # If right side is not sorted, then min is in the right side
            elif nums[mid] > nums[right]:
                left = mid + 1
            # If both side are sorted, then leftmost element is the min
            else:
                return nums[left]

        return None
