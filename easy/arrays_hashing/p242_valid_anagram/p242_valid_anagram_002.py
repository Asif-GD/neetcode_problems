class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # if the length of the two strings are different, they aren't anagrams
        if len(s) != len(t):
            return False
        else:
            # problem: this sorting returns a list, which takes up extra memory.
            # sorted_s = sorted(s)
            # sorted_t = sorted(t)

            # solution: apply string join.
            s = ''.join(sorted(s))
            t = ''.join(sorted(t))
            if s == t:
                return True

        return False
