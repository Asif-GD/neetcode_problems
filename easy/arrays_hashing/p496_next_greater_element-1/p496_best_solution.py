"""
check https://youtu.be/68a1Dc_qVq4 -> neetcode YT channel for an even better explanation.
"""

"""
Algorithm:
1. loop over elements in the superset - nums2.
2. while looping, when the current element is bigger than the top of stack
    - we pop the top of stack, find the index of the top of stack in nums1 (or the nums1_hashmap)
    - add the current element to the index at output list
3. if the element is present in the subset - nums1 (or the nums1_hashmap), we add it to the stack 
(we ONLY add it when it is present in nums1)
note: a hashmap is created to for efficient lookup of values and index of nums1 elements.
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    # hashmap
    nums1_map = {number: index for index, number in enumerate(nums1)}
    output = [-1] * len(nums1)
    stack = []

    # looping through the superset - nums2
    for number2 in nums2:
        # step 2
        while stack and stack[-1] < number2:
            value = stack.pop()
            index = nums1_map.get(value)
            output[index] = number2
        # step 3 - element is added to stack after checking the previous conditions
        # to ensure the next greatest number is immediately replaced.
        if number2 in nums1_map:
            stack.append(number2)

    return output


print(next_greater_element(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(next_greater_element(nums1=[2, 4], nums2=[1, 2, 3, 4]))
print(next_greater_element(nums1=[4, 1, 2], nums2=[2, 1, 3, 4]))
print(next_greater_element(nums1=[4, 1, 2], nums2=[1, 2, 3, 4]))
