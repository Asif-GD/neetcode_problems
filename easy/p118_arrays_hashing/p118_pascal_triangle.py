def generate(numRows: int) -> list[list[int]]:
    pascal_triangle = list()
    row_number = 0
    while row_number < numRows:
        current_row = list()
        length_of_row = row_number + 1
        # print(f"row_number, length_of_row = {row_number}")
        for column_number in range(0, length_of_row):
            # print(f"column_number = {column_number}")
            # for elements in start and end
            if column_number == 0 or column_number == length_of_row - 1:
                # print("inside if")
                current_row.append(1)
                # print(f"current_row = {current_row}")
            # for elements in the 2nd and the last but one'th position.
            elif column_number == 1 or column_number == length_of_row - 2:
                # print("inside elif")
                current_row.append(row_number)
                # print(f"current_row = {current_row}")
            # for the rest of the elements
            else:
                # print("inside else")
                # print(f"row_number = {row_number}")
                # print(f"column_number = {column_number}")
                element_to_add = pascal_triangle[row_number - 1][column_number - 1] \
                                 + pascal_triangle[row_number - 1][column_number]
                current_row.append(element_to_add)
                # print(f"current_row = {current_row}")
        pascal_triangle.append(current_row)
        # print(f"pascal_triangle = {pascal_triangle}")
        row_number += 1
    return pascal_triangle


print(generate(6))
