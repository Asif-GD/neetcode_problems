# without using division operator
# without using extra memory


class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        output_list: [list[int]] = [1] * len(nums)

        prefix: [int] = 1
        for index in range(len(nums)):
            output_list[index] = prefix
            prefix *= nums[index]

        postfix: [int] = 1
        for index in range(len(nums) - 1, -1, -1):
            output_list[index] *= postfix
            postfix *= nums[index]

        return output_list


print(Solution().product_except_self(nums=[1, 2, 3, 4]))
print(Solution().product_except_self(nums=[-1, 1, 0, -3, 3]))
