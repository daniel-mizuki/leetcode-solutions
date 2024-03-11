"""
Solution for Container With Most Water problem
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    """Solution for Container With Most Water problem"""

    def maxArea(self, height: List[int]) -> int:
        """
        Given an integer array height of length n. There are n vertical lines
        drawn such that the two endpoints of the ith line are (i, 0) and
        (i, height[i]).

        Returns the maximum amount of water a container can store.

        Args:
            height (List[int]): List of integers
        Returns:
            int: Maximum amount of water a container can store
        """

        max_area = 0
        max_height = max(height, default=0)

        left = 0
        right = len(height) - 1

        while (length := right - left) > 0:
            left_height = height[left]
            right_height = height[right]
            min_height = min(left_height, right_height)

            area = length * min_height
            max_area = max(max_area, area)

            if min_height == max_height:
                break

            if left_height <= right_height:
                while height[left] <= left_height and left < right:
                    left += 1
            if right_height <= left_height:
                while height[right] <= right_height and left < right:
                    right -= 1

        return max_area
