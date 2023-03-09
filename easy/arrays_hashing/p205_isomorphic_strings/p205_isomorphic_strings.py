def is_isomorphic(s: str, t: str) -> bool:
    char_map = dict()

    if len(set(s)) != len(set(t)):
        return False

    # since len(s) is always = len(t)
    for index in range(0, len(s)):
        # print(f"index = {index}")
        if s[index] in char_map.keys() and char_map[s[index]] != t[index]:
            # print("inside if")
            # print(f"s[index] = {s[index]}")
            # print(f"char_map.keys() = {char_map.keys()}")
            # print(f"char_map[s[index]] = {char_map[s[index]]}")
            # print(f"t[index] = {t[index]}")
            return False

        char_map.update({s[index]: t[index]})
        # print(f"char_map = {char_map}")
    return True


print(is_isomorphic(s="egg", t="add"))
print(is_isomorphic(s="foo", t="bar"))
print(is_isomorphic(s="paper", t="title"))

