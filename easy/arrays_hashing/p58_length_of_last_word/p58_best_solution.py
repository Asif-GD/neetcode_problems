# I was an idiot to not see this <facepalm>
# but using built-in methods kinda feels cheating

def length_of_last_word(s: str) -> int:
    s = s.strip(" ")
    s_list = s.split(" ")
    return len(s_list[-1])


print(length_of_last_word("this is my day"))
