# wrong answer - trying again
# success!

"""
1. It would be naive to assume that the words in list consists of only alphanumeric characters.
2. To account for that we have to send the encrypt-key along with the encoded message.

APPROACH
1. We prefix the word with its length followed by a delimiter - "4#word"
"""


class Solution:

    def encode(self, strs: list[str]) -> str:
        encode_string: [str] = ""
        for word in strs:
            encode_string += str(len(word)) + "#" + word

            # this can be simply put as '+ word' in previous loop
            # for char in word:
            #     encode_string += char

        return encode_string

    def decode(self, s: str) -> list[str]:
        decode_list: [list[str]] = list()
        pointer_1: [int] = 0
        word_size: [int] = 0

        def find_word_size(encode_s=s, index_s=pointer_1):
            temp_s: [str] = ''
            while encode_s[index_s] != '#':
                temp_s += encode_s[index_s]
                index_s += 1

            # to keep track of the index_s in main string
            nonlocal pointer_1
            pointer_1 = index_s + 1

            # gives us the word size
            size = int(temp_s.split(sep='#')[0])
            return size

        # print(find_word_size(encode_s='4#neet4#code4#love3#you', index_s=0))

        def extract_word(encode_s=s, index_s=pointer_1, w_size=word_size):
            word = encode_s[index_s: (index_s + w_size)]

            # to keep track of the index_s in main string
            nonlocal pointer_1
            pointer_1 += w_size

            return word

        # print(extract_word(encode_s='4#neet4#code4#love3#you', index_s=2, w_size=4, ))

        while pointer_1 < len(s):
            word_size = find_word_size(s, pointer_1)
            # print(word_size)
            word = extract_word(s, pointer_1, word_size)
            decode_list.append(word)
            # print(decode_list)

        return decode_list


sample_string_list_1 = ["neet", "code", "love", "you"]
decode_s_1 = "4#neet4#code4#love3#you"
sample_string_list_2 = ["we", "say", ":", "yes"]
decode_s_2 = "2#we3#say1#:3#yes"
sample_string_list_3 = [""]
decode_s_3 = "0#"

print(Solution().encode(strs=sample_string_list_1))
print(Solution().decode(s=decode_s_1))
print(Solution().encode(strs=sample_string_list_2))
print(Solution().decode(s=decode_s_2))
print(Solution().encode(strs=sample_string_list_3))
print(Solution().decode(s=decode_s_3))
