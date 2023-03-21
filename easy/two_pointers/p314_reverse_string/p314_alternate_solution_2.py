def reverse_string(s: list[str]) -> None:
    stack = list()
    for char in s:
        stack.append(char)

    for index in range(0, len(stack)):
        s[index] = stack.pop()


sample_string_1 = ["h", "e", "l", "l", "o"]
reverse_string(sample_string_1)
print(sample_string_1)

sample_string_2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(sample_string_2)
print(sample_string_2)
