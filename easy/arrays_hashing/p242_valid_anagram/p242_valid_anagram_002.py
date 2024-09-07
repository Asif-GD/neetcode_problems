class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # if the length of the two strings are different, they aren't anagrams
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False
