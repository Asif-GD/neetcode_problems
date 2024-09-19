# alternate solution
class Solution:
    def remove_anagrams(self, words: list[str]) -> list[str]:

        if len(words) == 1:
            return words

        sorted_words_list = [words[0]]

        for index in range(1, len(words)):
            if sorted(words[index]) != sorted(words[index - 1]):
                sorted_words_list.append(words[index])

        return sorted_words_list


print(Solution().remove_anagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
print(Solution().remove_anagrams(words=["a", "b", "c", "d", "e"]))
