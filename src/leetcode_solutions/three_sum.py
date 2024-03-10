"""
Solution for 3Sum problem
https://leetcode.com/problems/3sum/
"""

import bisect
import functools
from collections import Counter
from typing import List


@functools.cmp_to_key
def compare_triplets(t1: List[int], t2: List[int]) -> int:
    """
    Compare triplets
    """
    for i in range(3):
        if t1[i] < t2[i]:
            return -1
        if t1[i] > t2[i]:
            return 1
    return 0


class Solution:
    """
    Solution for 3Sum problem
    """

    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets
        [nums[i], nums[j], nums[k]] such that i != j, i != k,
        and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Args:
            nums (List[int]): List of integers
        Returns:
            List[List[int]]: List of triplets
        """

        res = []

        num_set = set(nums)
        sorted_nums = sorted(num_set)
        zero_pos = bisect.bisect(sorted_nums, 0)

        for neg_num in sorted_nums[:zero_pos]:
            num_set.remove(neg_num)
            for pos_num in sorted_nums[: zero_pos - 1 : -1]:
                complement = -(neg_num + pos_num)
                if complement in num_set and neg_num < complement < pos_num:
                    res.append([neg_num, -(neg_num + pos_num), pos_num])

        num_counts = Counter(nums)
        # Hande triplets with duplicate numbers
        for num, count in num_counts.items():
            triplet = None
            # Handle case for three 0s in triplet
            if num == 0 and count >= 3:
                triplet = [0, 0, 0]
            # Handle case for two of same number in triplet
            if num < 0 and count >= 2 and -2 * num in num_counts:
                triplet = [num, num, -2 * num]
            if num > 0 and count >= 2 and -2 * num in num_counts:
                triplet = [-2 * num, num, num]
            if triplet:
                bisect.insort(res, triplet, key=compare_triplets)

        return res
