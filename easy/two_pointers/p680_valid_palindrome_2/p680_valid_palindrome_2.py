def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            # pop left
            left_popped = s[left + 1: right + 1]
            left_popped_reversed = left_popped[::-1]
            # pop right
            right_popped = s[left: right]
            right_popped_reversed = right_popped[::-1]

            if left_popped == left_popped_reversed or right_popped == right_popped_reversed:
                return True
            else:
                return False

        left += 1
        right -= 1

    return True


print(is_palindrome(s="aba"))
print(is_palindrome(s="abca"))
print(is_palindrome(s="abc"))
print(is_palindrome(s="eeccccbebaeeabebccceea"))
print(is_palindrome(
    s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
print(is_palindrome(s="eedede"))
