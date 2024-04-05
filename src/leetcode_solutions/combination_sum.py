"""
Solution for Combination Sum problem
https://leetcode.com/problems/combination-sum/
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen numbers sum to target.
        You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two combinations are
        unique if the frequency
        of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations that sum up to target is less
        than 150 combinations for the given input.

        Args:
            candidates (List[int]): List of distinct integers
            target (int): Target
        Returns:
            List[List[int]]: List of all unique combinations
        """

        combinations = []

        for i, val in enumerate(candidates):
            if val == target:
                combinations.append([val])
            elif val < target:
                sub_combinations = self.combinationSum(candidates[i:], target - val)
                for combination in sub_combinations:
                    combination.append(val)
                combinations.extend(sub_combinations)

        return combinations
