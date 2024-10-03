from collections import Counter

sample_list: list[int] = [1, 1, 1, 2, 2, 3, 4, 4, 4, ]
counts = Counter(sample_list)
print(counts)

most_common = list()
for key, value in counts.items():
    print(key)
    print(value)
    if value >= 2:
        most_common.append(key)

# print(counts.most_common())
print(most_common)
