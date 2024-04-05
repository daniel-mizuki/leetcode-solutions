"""
Solution for Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
"""

from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        target_heap = self.large
        other_heap = self.small
        sign = 1

        if self.large and num < self.large[0]:
            target_heap, other_heap = other_heap, target_heap
            sign = -1

        if len(target_heap) <= len(other_heap):
            heappush(target_heap, sign * num)
        else:
            heappush(other_heap, -heappushpop(target_heap, sign * num))

    def findMedian(self) -> float:
        if not self.large:
            return None
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        if len(self.small) > len(self.large):
            return -self.small[0]
        return self.large[0]
