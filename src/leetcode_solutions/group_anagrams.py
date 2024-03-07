"""
Solution for Group Anagrams problem
"""

from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    """
    Solution for Group Anagrams problem
    """

    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together.

        Args:
            strs (List[str]): List of strings
        Returns:
            List[List[str]]: List of lists containing groups of anagrams
        """
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[frozenset(Counter(s).items())].append(s)

        return list(anagrams.values())

        # anagrams = defaultdict(list)
        # for s in strs:
        #     anagrams["".join(sorted(s))].append(s)

        # return list(anagrams.values())
