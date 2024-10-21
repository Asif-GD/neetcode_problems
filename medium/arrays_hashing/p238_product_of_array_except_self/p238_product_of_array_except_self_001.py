# brute-force approach
from math import prod


class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        output_list: [list[int]] = list()
        product: [int] = 1

        # edge-cases
        count_zero: [int] = nums.count(0)

        # When there are two or more zeros; the output will be zero.
        if count_zero >= 2:
            output_list = [0] * len(nums)

            return output_list
        # When there are one zero; the output will be zero in all the indices, except the zero-index.
        elif count_zero == 1:
            zero_index = nums.index(0)

            for number in nums:
                if number != 0:
                    product *= number

            for number in nums:
                if number != 0:
                    output_list.append(0)
                else:
                    output_list.append(product)

            return output_list

        else:
            product = prod(nums)
            for number in nums:
                output_list.append(int(product / number))

            return output_list


print(Solution().product_except_self(nums=[1, 2, 3, 4]))
print(Solution().product_except_self(nums=[-1, 1, 0, -3, 3]))
