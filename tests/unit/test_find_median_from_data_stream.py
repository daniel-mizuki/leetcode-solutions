"""
Tests for Find Median from Data Stream
"""

import pytest

from leetcode_solutions.find_median_from_data_stream import MedianFinder


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], None),
        ([1], 1.0),
        ([1, 2], 1.5),
        ([1, 2, 3], 2.0),
        ([1, 2, 3, 4], 2.5),
        ([1, 2, 3, 4, 5], 3.0),
        ([1, 2, 3, 4, 5, 6], 3.5),
        ([1, 2, 3, 4, 5, 6, 7], 4.0),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4.5),
        ([5, 6, 7, 8, 9, 1, 2, 3, 4, 10], 5.5),
        ([1, 1, 1, 1, 1000], 1.0),
    ],
)
def test_find_median_from_data_stream(nums, expected):
    """
    Test Find Median from Data Stream
    """
    obj = MedianFinder()
    for num in nums:
        obj.addNum(num)
    assert obj.findMedian() == expected
