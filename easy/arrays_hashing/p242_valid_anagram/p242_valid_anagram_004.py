from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(is_anagram("anagram", "nagaram"))
print(is_anagram("car", "rat"))
