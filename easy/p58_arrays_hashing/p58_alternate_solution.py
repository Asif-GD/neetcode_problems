# neetcode's solution
# when dealing with arrays and hashing problems, try solving it using pointers

def length_of_last_word(s: str) -> int:
    # we will be iterating it from reverse
    i = len(s) - 1
    word_length = 0
    # to eliminate trailing spaces
    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        word_length += 1
        i -= 1
    return word_length


print(length_of_last_word(" this is my day   "))
