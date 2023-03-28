def remove_duplicates(nums: list[int]) -> int:
    # brute-force approach
    left = 0
    right = 1
    while right != len(nums):
        if nums[left] == nums[right]:
            nums.pop(left)
        else:
            left += 1
            right += 1

    return len(nums)


print(remove_duplicates(nums=[1, 1, 2]))
print(remove_duplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
