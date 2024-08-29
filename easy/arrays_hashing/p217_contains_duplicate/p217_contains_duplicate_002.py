class Solution:
    def has_Duplicate(self, nums: list[int]) -> bool:
        pointer_1: [int] = 0

        while pointer_1 < len(nums):
            pointer_2: [int] = pointer_1 + 1

            while pointer_2 < len(nums):

                if nums[pointer_1] == nums[pointer_2]:
                    return True

                pointer_2 += 1

            pointer_1 += 1

        return False
