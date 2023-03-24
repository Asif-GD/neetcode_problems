def move_zeros(nums: list[int]) -> None:
    # note to self - start thinking in terms of concurrent executions.
    index = len(nums) - 1
    while index >= 0:
        if nums[index] == 0:
            nums.append(nums.pop(index))
        index -= 1


nums_1 = [0, 1, 0, 3, 12]
move_zeros(nums=nums_1)
print(nums_1)
