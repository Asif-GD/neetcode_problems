# group anagrams
class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        grouped_anagrams: list[list[str]] = list()
        # print(len(strs))
        if len(strs) == 1:
            return [strs]

        for item in strs:
            # print(f"inside for 1: {strs}")
            strs_copy = strs[::]
            # if len(strs_copy) == 1:
            #     grouped_anagrams.append(list(strs_copy))
            #     break
            # print(strs_copy)
            strs_copy.remove(item)

            temp_list: [list[str]] = list()
            temp_list.append(item)

            item_length = len(item)
            for item_copy in strs_copy:
                if len(item_copy) == item_length:
                    for index in range(len(item)):
                        if item.count(item[index]) != item_copy.count(item[index]):
                            break
                        elif index == item_length - 1:
                            temp_list.append(item_copy)

            grouped_anagrams.append(temp_list)
            for temp_list_item in temp_list:
                strs.remove(temp_list_item)

        grouped_anagrams.append(strs)
        return grouped_anagrams


print(Solution().group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().group_anagrams(strs=["",""]))
