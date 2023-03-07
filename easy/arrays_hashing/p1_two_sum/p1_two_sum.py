def two_sum(nums: list[int], target: int) -> list[int]:
    # because there is a guaranteed solution
    if len(nums) == 2:
        return [0, 1]
    current_index = 0
    for item in nums:
        remainder = target - item
        if remainder in nums[current_index + 1:]:
            return [current_index, nums.index(remainder, current_index + 1)]
        current_index += 1


print(two_sum([3, 2, 4], 6))
print(two_sum([3, 2, 3], 6))
print(two_sum([3, 3], 6))
