def two_sum(nums: list[int], target: int) -> list[int]:
    # because there is a guaranteed solution
    hash_map = dict()

    for index, number in enumerate(nums):
        difference = target - number
        if difference in hash_map:  # the current index will always be greater than the index of remainder in hashmap
            return [hash_map[difference], index]
        else:
            hash_map[number] = index

    return []


print(two_sum([3, 2, 4], 6))
print(two_sum([3, 2, 3], 6))
print(two_sum([3, 3], 6))
