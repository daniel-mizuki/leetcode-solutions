"""
Tests for Best Time to Buy and Sell Stock solution
"""

import pytest
from leetcode_solutions.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    "prices, solution",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([], 0),
        ([3, 3], 0),
        ([7, 6, 5, 4, 3, 4, 6, 1, 3], 3),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    ],
)
def test_max_profit(prices, solution):
    """
    Test Best Time to Buy and Sell Stock
    """
    assert Solution().maxProfit(prices) == solution
