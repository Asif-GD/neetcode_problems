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
