# exploring an alternate solution

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    map = defaultdict(list)

    for item in strs:

        count = [0] * 26

        # this becomes the key
        for char in item:
            count[ord(char) - ord('a')] += 1

        map[tuple(count)].append(item)

    return list(map.values())


print(group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(strs=["", ""]))
