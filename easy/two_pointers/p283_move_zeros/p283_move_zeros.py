def move_zeros(nums: list[int]) -> None:
    zero_count = nums.count(0)
    loop_count = 1

    while loop_count <= zero_count:
        zero_index = nums.index(0)

        # to move the zero to the last of the list
        for index in range(zero_index, len(nums) - loop_count):
            nums[index], nums[index + 1] = nums[index + 1], nums[index]

        loop_count += 1


nums_1 = [0, 1, 0, 3, 12]
move_zeros(nums=nums_1)
print(nums_1)
