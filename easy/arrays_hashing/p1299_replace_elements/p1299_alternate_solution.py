def replace_elements(arr: list[int]) -> list[int]:
    output_list = list()
    if len(arr) == 1:
        output_list.append(-1)
        return output_list
    else:
        current_index = 0
        for item in arr:
            if current_index == len(arr) - 1:
                output_list.append(-1)
                return output_list
            else:
                next_index = current_index + 1
                highest_to_the_right = max(arr[next_index:len(arr)])
                output_list.append(highest_to_the_right)
                current_index += 1


print(replace_elements([17, 18, 5, 4, 6, 1]))
