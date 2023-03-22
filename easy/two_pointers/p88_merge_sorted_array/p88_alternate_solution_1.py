def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for index, number in zip(range(m, m + n), nums2):
        nums1[index] = number
    nums1.sort()


nums_a, a = [1, 2, 3, 0, 0, 0], 3
nums_b, b = [2, 5, 6], 3
merge_sorted_array(nums1=nums_a, m=a, nums2=nums_b, n=b)
print(nums_a)
