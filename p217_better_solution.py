def contains_duplicate(self, nums: list[int]) -> bool:
    list_to_set = set(nums)
    # python sets does not take duplicates
    if len(list_to_set) < len(nums):
        return True
    else:
        return False
