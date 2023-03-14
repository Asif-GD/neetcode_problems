def find_maximum_balloons(text: str) -> int:
    count = 0
    text_map = {char: count for char in "balloon"}

    for char in text:
        if char in "balon":
            text_map[char] += 1

    # compensating for 2 Ls and Os in "balloon"
    text_map["l"] = int(text_map["l"] / 2)
    text_map["o"] = int(text_map["o"] / 2)

    least_count = min(text_map.values())

    return least_count


print(find_maximum_balloons("nlaebolko"))
print(find_maximum_balloons("loonbalxballpoon"))
print(find_maximum_balloons("leetcode"))
