def is_palindrome(s: str) -> bool:
    conditioned_s = "".join(char for char in s.lower() if char.isalnum())
    reversed_s = conditioned_s[::-1]
    return conditioned_s == reversed_s


print(is_palindrome(s="A man, a plan, a canal: Panama"))
print(is_palindrome(s="race a car"))
print(is_palindrome(s="."))
