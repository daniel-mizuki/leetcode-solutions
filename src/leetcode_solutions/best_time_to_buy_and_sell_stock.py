"""
Solution for Best Time to Buy and Sell Stock problem
"""

from typing import List


class Solution:
    """
    Solution for Best Time to Buy and Sell Stock problem
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit given a list of prices

        Args:
            prices (List[int]): List of prices, where prices[i] is the price
                of a given stock on the ith day

        Returns:
            int: Maximum profit
        """

        max_profit = 0

        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            elif (profit := price - min_price) > max_profit:
                max_profit = profit

        return max_profit
