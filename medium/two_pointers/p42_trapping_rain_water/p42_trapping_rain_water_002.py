# Neet Code Solution
"""
    min(left_max - right_max) - height[i]
    using two-pointers
"""


class Solution:
    def trap(self, height: list[int]) -> int:

        if not height: return 0

        left_pointer, right_pointer = 0, len(height) - 1
        left_max, right_max = height[left_pointer], height[right_pointer]
        total_trapped_rain_water = 0

        while left_pointer < right_pointer:
            if left_max <= right_max:
                left_pointer += 1
                left_max = max(left_max, height[left_pointer])
                total_trapped_rain_water += left_max - height[left_pointer]
            else:
                right_pointer -= 1
                right_max = max(right_max, height[right_pointer])
                total_trapped_rain_water += right_max - height[right_pointer]

        return total_trapped_rain_water


print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # output = 6
print(Solution().trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))  # output = 9
