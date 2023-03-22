def move_zeros(nums: list[int]) -> None:
    zero_count = nums.count(0)
    zero_list = [0] * zero_count
    for count in range(0, zero_count):
        nums.remove(0)
    nums.extend(zero_list)


nums_1 = [0, 1, 0, 3, 12]
move_zeros(nums=nums_1)
print(nums_1)
