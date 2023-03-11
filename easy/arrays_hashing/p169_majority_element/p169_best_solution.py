"""
using Boyer-Moore's algorithm
explanation:
since there is always a majority element with size > n/2
"""


def majority_element(nums: list[int]) -> int:
    result, count = 0, 0
    for number in nums:
        if count == 0:
            result = number
        count += (1 if number == result else -1)

    return result


print(majority_element(nums=[3, 2, 3]))
print(majority_element(nums=[2, 2, 1, 1, 1, 2, 2]))
print(majority_element(nums=[3, 3, 4]))
