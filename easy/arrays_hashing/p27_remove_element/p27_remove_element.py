def remove_element(nums: list[int], val: int) -> int:
    number_of_val_in_nums = nums.count(val)
    output = len(nums) - number_of_val_in_nums
    if number_of_val_in_nums != 0:
        for loop_number in range(0, number_of_val_in_nums):
            nums.remove(val)
            # nums.append("_") -> not necessary
    return output


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
