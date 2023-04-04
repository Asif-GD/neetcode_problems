# NOTE - although this is correct, it doesn't pass the assertion on leetcode. 


def remove_duplicates(nums: list[int]) -> list[int] and int:
    nums = list(set(nums))
    # print(nums)
    nums.sort()
    return nums, len(nums)


print(remove_duplicates(nums=[1, 1, 2]))
print(remove_duplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
