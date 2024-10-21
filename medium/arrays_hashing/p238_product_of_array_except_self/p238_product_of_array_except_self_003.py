# without using division operator
"""
exceeds time limit on one test case.
"""
from math import prod


class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        output_list: [list[int]] = list()

        prefix_prod: [list[int]] = list()
        postfix_prod: [list[int]] = list()

        for index in range(len(nums)):
            prefix_prod.append(prod(nums[:index + 1]))
            postfix_prod.append(prod(nums[index:]))

        # print(prefix_prod, postfix_prod)

        for index in range(len(nums)):
            result: [int] = int()

            if index == 0:
                result = postfix_prod[index + 1]
                output_list.append(result)
            elif index == len(nums) - 1:
                result = prefix_prod[index - 1]
                output_list.append(result)
            else:
                result = prefix_prod[index - 1] * postfix_prod[index + 1]
                output_list.append(result)

        return output_list


print(Solution().product_except_self(nums=[1, 2, 3, 4]))
print(Solution().product_except_self(nums=[-1, 1, 0, -3, 3]))
