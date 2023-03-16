def is_word_pattern(pattern: str, s: str) -> bool:
    char_map = dict()
    s_list = s.split()
    if len(pattern) != len(s_list):
        return False
    for index, char in enumerate(pattern):
        if char not in char_map.keys():
            if s_list[index] not in char_map.values():
                char_map[char] = s_list[index]
            else:
                return False
        # checking if char in pattern is not already mapped to a different value
        elif char_map[char] != s_list[index]:
            return False

    return True


print(is_word_pattern(pattern="abba", s="dog cat cat dog"))
print(is_word_pattern(pattern="abba", s="dog cat cat fish"))
print(is_word_pattern(pattern="aaaa", s="dog cat cat dog"))
print(is_word_pattern(pattern="abba", s="dog dog dog dog"))
