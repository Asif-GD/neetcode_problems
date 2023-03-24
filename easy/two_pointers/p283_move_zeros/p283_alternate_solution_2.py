def move_zeros(nums: list[int]) -> None:
    nums[:] = [n for n in nums if n != 0] + [0] * nums.count(0)


nums_1 = [0, 1, 0, 3, 12]
move_zeros(nums=nums_1)
print(nums_1)
