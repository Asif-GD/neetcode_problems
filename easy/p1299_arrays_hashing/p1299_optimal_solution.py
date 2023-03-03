# neetcode's solution
# initial max = -1
# we iterate through the array in reverse
# compare initial max to the previous element in the array

def replace_elements(arr: list[int]) -> list[int]:
    if len(arr) == 1:
        arr[-1] = -1
        return arr
    current_max = -1
    for index in range(len(arr) - 1, -1, -1):
        new_max = max(current_max, arr[index])
        arr[index] = current_max
        current_max = new_max
    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
