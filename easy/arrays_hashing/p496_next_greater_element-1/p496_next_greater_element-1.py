def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    output = list()

    for number1 in nums1:
        number1_position = nums2.index(number1)
        for index in range(number1_position + 1, len(nums2)):
            if nums2[index] > number1:
                output.append(nums2[index])
                break
            elif index == len(nums2) - 1:
                output.append(-1)
                break

    return output


print(next_greater_element(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(next_greater_element(nums1=[2, 4], nums2=[1, 2, 3, 4]))
