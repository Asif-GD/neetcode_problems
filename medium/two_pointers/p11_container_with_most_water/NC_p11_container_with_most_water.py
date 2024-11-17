# using two-pointer approach
"""
o(n) time
"""


class Solution:
    def max_area(self, height: list[int]) -> int:
        res_area: [int] = 0

        left_pointer: [int] = 0
        right_pointer: [int] = len(height) - 1

        while left_pointer < right_pointer:
            area: [int] = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            res_area = max(res_area, area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return res_area


print(Solution().max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # output: 49
print(Solution().max_area(height=[1, 1]))  # output: 1
print(Solution().max_area(height=[1, 7, 2, 5, 4, 7, 3, 6]))  # output: 36
