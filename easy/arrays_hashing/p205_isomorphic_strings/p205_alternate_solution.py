def is_isomorphic(s: str, t: str) -> bool:
    char_map = {}

    for index, char in enumerate(s):
        if char not in char_map:
            if t[index] not in char_map.values():
                char_map[char] = t[index]
            else:
                return False
        elif char_map[char] != t[index]:
            return False
    return True


print(is_isomorphic(s="egg", t="add"))
print(is_isomorphic(s="foo", t="bar"))
print(is_isomorphic(s="paper", t="title"))
print(is_isomorphic(s="baba", t="aabb"))
