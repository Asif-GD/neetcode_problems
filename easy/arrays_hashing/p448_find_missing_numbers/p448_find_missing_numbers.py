def find_missing_numbers(nums: list[int]) -> list[int]:
    output = list()
    nums_set = set(nums)
    for number in range(1, len(nums) + 1):  # to loop from 1 to n
        if number not in nums_set:
            output.append(number)
        else:
            nums_set.remove(number)

    return output


print(find_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_missing_numbers([1, 1]))
# print(find_missing_numbers([1, 3, 5, 7]))
