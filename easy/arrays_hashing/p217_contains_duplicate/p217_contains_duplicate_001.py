def contains_duplicate(self, nums: list[int]) -> bool:
    # sorting the list so the duplicate numbers get grouped.
    nums.sort()
    start_index = 0
    while True:
        next_index = start_index + 1
        # if there is only one number in the list
        if len(nums) == 1:
            return False
        # if the starting index has reached the end of the list
        elif start_index == len(nums) - 1:
            return False
        # compare the current item and the next item
        else:
            current_item = nums[start_index]
            next_item = nums[next_index]
            if current_item == next_item:
                return True
            else:
                start_index += 1
