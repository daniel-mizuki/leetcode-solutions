"""
Solution for Top K Frequent Elements problem
https://leetcode.com/problems/top-k-frequent-elements/
"""

from collections import Counter
from typing import List


class Solution:
    """
    Solution for Top K Frequent Elements
    """

    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most
        frequent elements.

        Args:
            nums (List[int]): List of integers
            k (int): Number of most frequent elements
        Returns:
            List[int]: List of k most frequent elements
        """
        return [e[0] for e in Counter(nums).most_common(k)]
