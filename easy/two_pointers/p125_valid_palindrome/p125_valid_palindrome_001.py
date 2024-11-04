class Solution:
    def is_palindrome(self, s: str) -> bool:

        clean_text: [str] = "".join(char for char in s if char.isalnum()).lower()
        # print(f"clean_text,length: {clean_text, len(clean_text)}")

        # checking edge-case
        if len(clean_text) == 0:
            return True

        left_pointer: [int] = 0
        right_pointer: [int] = len(clean_text) - 1

        while left_pointer <= right_pointer:
            # print(f"1,2: {left_pointer, right_pointer}")
            if clean_text[left_pointer] != clean_text[right_pointer]:
                # print(f"1,2: {left_pointer, right_pointer}")
                return False
            left_pointer += 1
            right_pointer -= 1

        return True


print(Solution().is_palindrome(s="Was it a car or a cat I saw?"))
print(Solution().is_palindrome(s="tab a cat"))
print(Solution().is_palindrome(s=" "))
print(Solution().is_palindrome(s="No lemon, no melon"))
