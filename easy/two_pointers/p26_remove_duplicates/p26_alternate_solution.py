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
