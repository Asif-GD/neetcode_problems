"""
https://youtu.be/jJXJ16kPFWg
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not is_alpha_num(s[left]):
            left += 1
        while right > left and not is_alpha_num(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def is_alpha_num(char: str) -> bool:
    return (ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))


print(is_palindrome(s="A man, a plan, a canal: Panama"))
print(is_palindrome(s="race a car"))
print(is_palindrome(s="."))
