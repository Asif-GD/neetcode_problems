"""
the idea remains the same, but the implementation is different
"""


def pivot_index(nums: list[int]) -> int:
    sum_left, sum_right = 0, sum(nums)

    for index, number in enumerate(nums):
        sum_right -= number
        if sum_left == sum_right:
            return index
        sum_left += number
    return -1


print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([-1, -1, -1, -1, 0, 1]))
