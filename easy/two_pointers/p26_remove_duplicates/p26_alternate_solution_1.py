def remove_duplicates(nums: list[int]) -> int:
    left, right = 1, 1

    while right != len(nums):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
            right += 1
        else:
            right += 1

    return left


print(remove_duplicates(nums=[1, 1, 2]))
print(remove_duplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
