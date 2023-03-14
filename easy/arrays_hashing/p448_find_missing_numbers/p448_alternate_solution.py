"""
Algorithm:
1. we loop through all the numbers in nums
-- since one of the constraint is 1 <= nums[i] <= n, meaning there can never be a number higher than n
so, we calculate the index of number (number - 1) and simply negate the value that is available at nums[index]
-- as we are changing the input array, we ensure to take the absolute value of the number because they can be negative too
2. in the second loop, if the number is positive, we simply return its (index + 1) in the output list.
"""


def find_missing_numbers(nums: list[int]) -> list[int]:
    output = list()

    for number in nums:
        num_index = abs(number) - 1
        nums[num_index] = abs(nums[num_index]) * -1

    for index, number in enumerate(nums):
        if number > 0:
            output.append(index + 1)

    return output


print(find_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_missing_numbers([1, 1]))
