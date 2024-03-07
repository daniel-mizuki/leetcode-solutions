import pytest
from leetcode_solutions.contains_duplicate import Solution


@pytest.mark.parametrize(
    "nums, solution",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(nums, solution):
    assert Solution().containsDuplicate(nums) == solution
