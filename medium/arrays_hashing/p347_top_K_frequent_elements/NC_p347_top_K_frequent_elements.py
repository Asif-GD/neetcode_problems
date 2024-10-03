from collections import Counter


class Solution:
    def top_K_Frequent(self, nums: list[int], k: int) -> list[int]:

        # counting the items and mapping them.
        count_map: [int] = dict()
        for item in nums:
            # count_map[item] += 1
            # count_map[item] = 1 + count_map[item]
            """
            the above might result in error when item isn't already in the dict, so we use .get()
            """
            count_map[item] = 1 + count_map.get(item, 0)

        # sorting the items based on their count
        frequency_sort: [list[int]] = [[] for n in range(len(nums) + 1)]
        for key, value in count_map.items():
            frequency_sort[value].append(key)

        # getting the k_most frequent items
        k_most_frequent: list[int] = list()
        for item in range(len(frequency_sort) - 1, 0, -1):
            for sub_item in frequency_sort[item]:  # because it's a [[]]
                k_most_frequent.append(sub_item)
                if len(k_most_frequent) == k:
                    return k_most_frequent


print(Solution().top_K_Frequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # output [1,2]
print(Solution().top_K_Frequent(nums=[1], k=1))  # output [1]
print(Solution().top_K_Frequent(nums=[1, 2], k=2))  # output [1,2]
print(Solution().top_K_Frequent(nums=[7, 7], k=1))  # output [7]
print(Solution().top_K_Frequent(nums=[1, 2, 2, 3, 3, 3], k=2))  # output [3,2]
