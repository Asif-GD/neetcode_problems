"""
Algorithm:
start from the left -> because they have asked us to find only the left-most pivot index
"""


def pivot_index(nums: list[int]) -> int:
    nums = [0] + nums + [0]
    output = -1
    # print(f"nums = {nums}")
    for index in range(1, len(nums) - 1):
        # print(f"index = {index}")
        # this is what contributes to a lot of time. calculating the sum at each index
        sum_left = sum(nums[:index])
        sum_right = sum(nums[index + 1:])
        # print(f"sum_left <-> sum_right = {sum_left} <-> {sum_right}")
        if sum_left == sum_right:
            output = index - 1  # to counter the addition of zero at start
            break

    return output


print(pivot_index([1, 7, 3, 6, 5, 6]))
