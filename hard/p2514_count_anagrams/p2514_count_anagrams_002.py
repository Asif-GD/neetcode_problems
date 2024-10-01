from math import factorial
from collections import Counter


class Solution:
    def count_anagrams(self, s: str) -> int:

        def display(word):
            word_factorial = factorial(len(word))

            """
            explanation:
            A factorial of a word is a count of all the possible combinations of the letters from that word. 
            Normally, this wouldn't be an issue if all letters in the word are unique.
            
            eg: factorial of "too" will be "too(123), too(132), oto(213), oot(231), oto(312), oot(321)"; 
            but only 3 unique combinations of the letters are present.
            
            What we require is the permutation of the word.
            In order to get the permutation; 
                the formula is factorial(len(word)) / factorial( len(word) - len(unique_char_in_word) )
            """
            """
            So we create a dict using Counter(); to count the number of times a char appears in the word.
            Then perform floor division on the factorial, for all the values in Counter.dict()
            """
            # a Counter() takes a iterable and returns it as a dict with item as key and their count as value pairs.
            for value in Counter(word).values():
                word_factorial //= factorial(value)

            return word_factorial

        possible_anagrams: [int] = 1
        for word in s.split():
            possible_anagrams *= display(word)

        return possible_anagrams % ((10 ** 9) + 7)


print(Solution().count_anagrams(s="too hot"))
print(Solution().count_anagrams(s="aa"))
print(Solution().count_anagrams(s="ptx cccbhbq"))
