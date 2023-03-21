def reverse_string(s: list[str]) -> None:
    def reverse(left: int, right: int):
        if left < right:
            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)

    reverse(0, len(s) - 1)


sample_string_1 = ["h", "e", "l", "l", "o"]
reverse_string(sample_string_1)
print(sample_string_1)

sample_string_2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(sample_string_2)
print(sample_string_2)
