class Solution:
    def remove_anagrams(self, words: list[str]) -> list[str]:

        if len(words) == 1:
            return words

        index = 1
        while index < len(words):
            if sorted(words[index]) == sorted(words[index - 1]):
                words.remove(words[index])
            else:
                index += 1

        return words


print(Solution().remove_anagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
print(Solution().remove_anagrams(words=["a", "b", "c", "d", "e"]))
