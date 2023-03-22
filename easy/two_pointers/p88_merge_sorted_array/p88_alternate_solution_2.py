def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # if m == 0:
    #     for index, number in enumerate(nums2):
    #         nums1[index] = number
    # # why doesn't this work?
    # # if m == 0:
    # #     nums1 = nums2
    # else:
    index = m + n - 1

    # merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[index] = nums1[m - 1]
            m -= 1
        else:
            nums1[index] = nums2[n - 1]
            n -= 1
        index -= 1

    # fill leftover nums2 elements
    while n > 0:
        nums1[index] = nums2[n - 1]
        n, index = n - 1, index - 1


nums_a, a = [1, 2, 3, 0, 0, 0], 3
nums_b, b = [2, 5, 6], 3
merge_sorted_array(nums1=nums_a, m=a, nums2=nums_b, n=b)
print(nums_a)

nums_c, c = [0], 0
nums_d, d = [1], 1
merge_sorted_array(nums1=nums_c, m=c, nums2=nums_d, n=d)
print(nums_c)
