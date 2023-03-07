def is_subsequence(self, s: str, t: str) -> bool:
    # s can't be a substring if it contains more chars than t
    if len(s) > len(t):
        return False
    # initiating lists for checks
    char_position_list = list()
    temp_list = list()
    for char in s:
        # eg: s = 'aaaaaa' and t = 'bbaaaa'; s can't be a substring
        if s.count(char) > t.count(char):
            return False
        char_position = t.find(char)
        # t = t.replace(char,"0",1)
        if char_position == -1:
            return False
        char_position_list.append(char_position)
        if len(char_position_list) > 1:
            temp_list = char_position_list[:]
            temp_list.sort()
            # if char positions in s aren't ascending, it can't be a substring
            if char_position_list != temp_list:
                return False
    return True
