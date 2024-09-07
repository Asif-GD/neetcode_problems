def two_sum(nums: list[int], target: int) -> list[int]:
    solution = list()
    # because there is a guaranteed solution
    hash_map = dict()

    for index in range(len(nums)):
        remainder = target - nums[index]
        if remainder in hash_map:
            solution.append(index)
            solution.append(hash_map[remainder])
        else:
            hash_map[nums[index]] = index

    solution.sort()
    return solution


print(two_sum([3, 2, 4], 6))
print(two_sum([3, 2, 3], 6))
print(two_sum([3, 3], 6))
