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

        num_counts = Counter(nums)
        sorted_nums = sorted(num_counts.keys())
        neg_end = bisect.bisect(sorted_nums, -1)
        pos_start = bisect.bisect(sorted_nums, 0)

        for neg_num in sorted_nums[:neg_end]:

            # Handle case for two of same negative number in triplet
            complement = -2 * neg_num
            if num_counts[neg_num] >= 2 and complement in num_counts:
                res.append([neg_num, neg_num, complement])

            # Handle general case
            for pos_num in sorted_nums[: pos_start - 1 : -1]:
                complement = -(neg_num + pos_num)
                if complement in num_counts and neg_num < complement < pos_num:
                    res.append([neg_num, complement, pos_num])

            # Handle case for two of same positive number in triplet
            complement = -neg_num / 2
            if num_counts[complement] >= 2:
                res.append([neg_num, complement, complement])

            del num_counts[neg_num]

        # Handle case for three 0s in triplet
        if num_counts[0] >= 3:
            res.append([0, 0, 0])

        return res
