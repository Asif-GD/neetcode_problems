def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    output = [-1] * len(nums1)

    for index_1, number1 in enumerate(nums1):
        number1_position = nums2.index(number1)
        for index_2 in range(number1_position + 1, len(nums2)):
            if nums2[index_2] > number1:
                output[index_1] = nums2[index_2]
                break

    return output


print(next_greater_element(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(next_greater_element(nums1=[2, 4], nums2=[1, 2, 3, 4]))
