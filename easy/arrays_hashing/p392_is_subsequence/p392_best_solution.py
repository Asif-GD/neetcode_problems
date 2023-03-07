def is_subsequence(s: str, t: str) -> bool:
    pos = 0
    for i in s:
        # print(f"i = {i}")
        pos = t.find(i)
        # print(f"pos = {pos}")
        if pos == -1:
            return False
        # understand what this expression means
        # ans - he drops all the chars that were before the current position in t.
        # t[something : ] means that position to end.
        t = t[pos + 1:]
        # print(f"t = {t}")
    return True


print(is_subsequence("aaaaaa", "bbaaaa"))
