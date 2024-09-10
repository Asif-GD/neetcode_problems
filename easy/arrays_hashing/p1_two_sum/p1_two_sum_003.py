from typing import Dict


def two_sum(nums: list[int], target: int) -> list[int]:
    solution: list[int] = list()
    # because there is a guaranteed solution
    hash_map: dict[int, int] = dict()

    for index in range(len(nums)):
        remainder = target - nums[index]
        if remainder in hash_map:  # the current index will always be greater than the index of remainder in hashmap
            solution.append(hash_map[remainder])
            solution.append(index)
        else:
            hash_map[nums[index]] = index

    return solution


print(two_sum([3, 2, 4], 6))
print(two_sum([3, 2, 3], 6))
print(two_sum([3, 3], 6))
