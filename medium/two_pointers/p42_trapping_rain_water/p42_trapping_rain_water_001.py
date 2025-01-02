# Neet Code Solution
"""
    min(left_max - right_max) - height[i]
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left_max_at_i: [list[int]] = [0, ]
        current_left_max: [int] = 0
        for index in range(1, len(height)):
            left_max_at_i.append(max(height[index - 1], current_left_max))
            if height[index - 1] > current_left_max:
                current_left_max = height[index - 1]

        # print(left_max_at_i)

        right_max_at_i: [list[int]] = [0, ]
        current_right_max: [int] = 0
        for index in range(len(height) - 2, -1, -1):  # --> 2
            right_max_at_i.append(max(height[index + 1], current_right_max))
            if height[index + 1] > current_right_max:
                current_right_max = height[index + 1]

        # although we calculate it from the reverse (see #2), we still add the elements normally,
        # hence the list is reversed after.
        right_max_at_i.reverse()
        # print(right_max_at_i)

        # trapped_rain_water_at_index: [list[int]] = []
        total_trapped_rain_water: [int] = 0
        for index in range(0, len(height)):
            rain_water_at_index = min(left_max_at_i[index], right_max_at_i[index]) - height[index]
            total_trapped_rain_water += max(0, rain_water_at_index)

        return total_trapped_rain_water


print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # output = 6
print(Solution().trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))  # output = 9
