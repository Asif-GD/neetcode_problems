def length_of_last_word(s: str) -> int:
    s = s.rstrip()
    if len(s) == 1:
        return 1
    # word_size = 0
    for char in range(len(s) - 1, -1, -1):
        if s[char] == ' ':
            return len(s) - char - 1
    return len(s)
