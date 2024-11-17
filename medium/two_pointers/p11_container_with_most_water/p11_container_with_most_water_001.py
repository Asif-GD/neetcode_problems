# BRUTE force approach
"""
o(n^2) time
"""


class Solution:
    def max_area(self, height: list[int]) -> int:

        res_area: [int] = 0

        for first_pointer in range(len(height)):
            for second_pointer in range(first_pointer + 1, len(height)):
                area: [int] = (second_pointer - first_pointer) * min(height[first_pointer], height[second_pointer])

                res_area = max(res_area, area)

        return res_area


print(Solution().max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # output: 49
print(Solution().max_area(height=[1, 1]))  # output: 1
