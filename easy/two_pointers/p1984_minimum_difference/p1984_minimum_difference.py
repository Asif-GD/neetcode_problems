"""
Explanation -
The problem requires us to find the difference between the highest and lowest amongst a certain number of
students from a list.
Return the least difference after calculation.

nums[int] - scores of all students
k - the number students to compare at a time.

So, a sliding window makes this easier. But the list has to be sorted first.
This way the first student will have the lowest score and the last student will have the highest score.
(sort is ascending by default)
"""


def minimum_difference(nums: list[int], k: int) -> int:
    start = 0
    stop = k - 1
    nums.sort(reverse=True)
    least_difference = max(nums)  # this way the least difference can never be bigger than this.
    while stop < len(nums):
        least_difference = min(least_difference, nums[start] - nums[stop])
        start += 1
        stop += 1

    return least_difference


print(minimum_difference(nums=[90], k=1))
print(minimum_difference(nums=[9, 4, 1, 7], k=2))
print(minimum_difference(nums=[87063, 61094, 44530, 21297, 95857, 93551, 9918], k=6))
