def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1.extend(nums2)
    for count in range(0, n):
        nums1.remove(0)
    nums1.sort()


nums_a, a = [1, 2, 3, 0, 0, 0], 3
nums_b, b = [2, 5, 6], 3
merge_sorted_array(nums1=nums_a, m=a, nums2=nums_b, n=b)
print(nums_a)
