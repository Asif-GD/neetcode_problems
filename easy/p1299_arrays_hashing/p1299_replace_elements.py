def replace_elements(arr: list[int]) -> list[int]:
    output_list = list()
    if len(arr) == 1:
        output_list.append(-1)
        return output_list
    else:
        for index in range(0, len(arr)):
            temp_arr = arr.copy()
            if len(temp_arr) == 1:
                output_list.append(-1)
                return output_list
            else:
                temp_arr.pop(0)
                temp_arr.sort(reverse=True)
                output_list.append(temp_arr[0])
                arr.pop(0)
