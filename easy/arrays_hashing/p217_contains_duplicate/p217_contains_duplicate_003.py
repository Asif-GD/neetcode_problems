class Solution:
    """
    PROBLEMS with this solution 002
    1. doesn't address the situation where the list contains only one element;
    in that case no check would be required.
    2. it's more efficient to sort the list first.
    3. can be made using one loop in place of two.
    """

    def has_Duplicate(self, nums: list[int]) -> bool:

        # if the list contains only one element (edge case)
        if len(nums) == 1:
            return False

        # sort the list for efficiency
        nums.sort()

        pointer_1: [int] = 0
        pointer_2: [int] = 0
        while pointer_2 != len(nums) - 1:
            pointer_2: [int] = pointer_1 + 1

            if nums[pointer_1] == nums[pointer_2]:
                return True

            pointer_1 += 1

        return False
