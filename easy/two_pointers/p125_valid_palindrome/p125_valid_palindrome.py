def is_palindrome(s: str) -> bool:
    conditioned_s = s.lower()

    # to remove all non-alphanumeric
    for char in conditioned_s:
        if char not in "abcdefghijklmnopqrstuvwxyz0123456789":
            conditioned_s = conditioned_s.replace(char, "")

    if conditioned_s == "":
        return True

    first_char = 0
    last_char = len(conditioned_s) - 1

    while first_char <= int(len(conditioned_s) / 2):
        if conditioned_s[first_char] != conditioned_s[last_char]:
            return False

        first_char += 1
        last_char -= 1

    return True


print(is_palindrome(s="A man, a plan, a canal: Panama"))
print(is_palindrome(s="race a car"))
print(is_palindrome(s="."))
