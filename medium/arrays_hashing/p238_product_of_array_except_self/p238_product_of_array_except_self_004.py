# without using division operator
# without using extra memory
"""
exceeds time limit on one test case.
"""
from math import prod


class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        output_list: [list[int]] = list()

        for index in range(len(nums)):
            result: [int] = int()

            if index == 0:
                result = prod(nums[index + 1:])
                output_list.append(result)
            elif index == len(nums) - 1:
                result = prod(nums[:index])
                output_list.append(result)
            else:
                result = prod(nums[:index]) * prod(nums[index + 1:])
                output_list.append(result)

        return output_list


print(Solution().product_except_self(nums=[1, 2, 3, 4]))
print(Solution().product_except_self(nums=[-1, 1, 0, -3, 3]))
