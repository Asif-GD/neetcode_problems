"""
won't work all the time because of test case 5.
"""


def is_word_pattern(pattern: str, s: str) -> bool:
    mapping = dict()
    s_list = s.split()
    if len(pattern) != len(s_list):
        return False
    # mapping pattern to s
    for index, char in enumerate(pattern):
        if char not in mapping:
            mapping[char] = s_list[index]
        # checking if char in pattern is not already mapped to a different value
        elif mapping[char] != s_list[index]:
            return False

    # mapping s to pattern
    for index, word in enumerate(s_list):
        if word not in mapping:
            mapping[word] = pattern[index]
        # checking if word in s_list is not already mapped to a different char
        elif mapping[word] != pattern[index]:
            return False

    return True


print(is_word_pattern(pattern="abba", s="dog cat cat dog"))
print(is_word_pattern(pattern="abba", s="dog cat cat fish"))
print(is_word_pattern(pattern="aaaa", s="dog cat cat dog"))
print(is_word_pattern(pattern="abba", s="dog dog dog dog"))
print(is_word_pattern(pattern="abc", s="b c a"))
