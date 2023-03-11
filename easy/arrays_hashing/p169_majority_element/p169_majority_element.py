def majority_element(nums: list[int]) -> int:
    element_count = dict()
    for number in nums:
        if number not in element_count:
            element_count[number] = 1
        else:
            element_count[number] += 1
    number_with_max_count = max(element_count, key=element_count.get)
    return number_with_max_count


print(majority_element(nums=[3, 2, 3]))
print(majority_element(nums=[2, 2, 1, 1, 1, 2, 2]))
print(majority_element(nums=[3, 3, 4]))
