# exploring an alternate solution

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    result = []

    # for item in strs; we sort it as a tuple, which becomes the key in the anagrams dictionary
    # we add the item to the corresponding sorted_item
    for item in strs:
        sorted_item = tuple(sorted(item))
        # print(f"sorted_item: {sorted_item}")
        anagrams[sorted_item].append(item)

    # print(f"anagrams: {anagrams}")

    for value in anagrams.values():
        result.append(value)
    return result


print(group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(strs=["", ""]))
