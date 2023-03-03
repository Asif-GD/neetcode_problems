sample_list = list()
temp_list = list()

temp_list.append(10)
temp_list = temp_list * 5
sample_list.extend(temp_list)
print(temp_list)
print(sample_list)

sample_list_2 = [12, 2, 4, 5, 23, 6, 7]
number = max(sample_list_2[2:5])
print(number)