# wrong answer

from math import factorial


class Solution:
    def count_anagrams(self, s: str) -> int:
        s_list: [list[str]] = s.split()  # return s as a list of string separated at whitespaces
        count: [int] = 1

        if len(s_list) == 1:
            return 1

        for item in s_list:
            # print(f"count: {count}; item: {item}")
            count *= factorial(len(item))
            # print(count)

        possible_anagrams = count / len(s_list)
        # print(possible_anagrams)

        return int(possible_anagrams % (10 ** 9 + 7))


print(Solution().count_anagrams(s="too hot"))
print(Solution().count_anagrams(s="aa"))
print(Solution().count_anagrams(s="ptx cccbhbq"))
