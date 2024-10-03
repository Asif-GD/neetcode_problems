from collections import Counter


class Solution:
    def top_K_Frequent(self, nums: list[int], k: int) -> list[int]:
        k_most_frequent: list[int] = list()

        counter = Counter(nums)

        for item in counter.most_common(n=k):
            k_most_frequent.append(item[0])

        return k_most_frequent


print(Solution().top_K_Frequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(Solution().top_K_Frequent(nums=[1], k=1))
print(Solution().top_K_Frequent(nums=[1, 2], k=2))
