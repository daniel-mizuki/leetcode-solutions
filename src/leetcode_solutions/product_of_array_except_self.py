"""
Solution for Product of Array Except Self problem
https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    """
    Solution for Product of Array Except Self problem
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that
        answer[i] is equal to the product of all the elements of nums
        except nums[i].

        Args:
            nums (List[int]): List of integers
        Returns:
            List[int]: List of products
        """

        answer = [1] * len(nums)

        prefix = 1
        for i, n in enumerate(nums):
            answer[i] = prefix
            prefix *= n

        suffix = 1
        for i, n in reversed(list(enumerate(nums))):
            answer[i] *= suffix
            suffix *= n

        return answer
