# group anagrams
from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        # using a default dict will prevent errors in case the char is missing
        result_hashmap = defaultdict(list)  # mapping charCount to list of Anagrams
        # print(result_hashmap.values())

        for item in strs:
            count = [0] * 26  # creating a list of indices representing a ... z for each item; this becomes the key.
            # print(f"count-> {count}")

            for char in item:
                """
                because we know that all char are from a - z; the following code will give us the index
                # unicode of 'char' - unicode of 'a'
                """
                count[ord(char) - ord('a')] += 1

            # print(f"count-> {count}")

            # using a tuple because they are immutable in python. dict keys are to be immutable.
            result_hashmap[tuple(count)].append(item)

        grouped_anagrams = list(result_hashmap.values())

        # print(f"final result_hashmap: {result_hashmap}")

        return grouped_anagrams


print(Solution().group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().group_anagrams(strs=["", ""]))
