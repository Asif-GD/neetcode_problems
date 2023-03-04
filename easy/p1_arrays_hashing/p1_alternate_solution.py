# neetcode solution

def two_sum(nums: list[int], target: int) -> list[int]:
    # because there is a guaranteed solution
    if len(nums) == 2:
        return [0, 1]
    hashmap = {}
    for current_index, value in enumerate(nums):
        remainder = target - value
        if remainder in hashmap:
            return [hashmap[remainder], current_index]
        hashmap[value] = current_index


print(two_sum([3, 2, 4], 6))
print(two_sum([3, 2, 3], 6))
print(two_sum([3, 3], 6))
