def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # using hashmaps
    map_s, map_t = dict(), dict()

    # building the hashmaps
    for index in range(len(s)):  # since len(s) is always equal to len(t)
        map_s[s[index]] = 1 + map_s.get(s[index], 0)
        map_t[t[index]] = 1 + map_t.get(t[index], 0)

    # checking if they are equal
    for char in map_s:
        if map_s[char] != map_t.get(char, 0):
            return False

    return True


print(is_anagram("anagram", "nagaram"))
print(is_anagram("car", "rat"))
