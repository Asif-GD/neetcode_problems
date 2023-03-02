def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    else:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True

    return False
