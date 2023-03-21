def reverse_string(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left <= right:
        # a temp variable isn't required because in python the next line is executed simultaneously.
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


sample_string_1 = ["h", "e", "l", "l", "o"]
reverse_string(sample_string_1)
print(sample_string_1)

sample_string_2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(sample_string_2)
print(sample_string_2)
