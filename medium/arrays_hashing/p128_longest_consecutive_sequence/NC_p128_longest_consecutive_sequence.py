class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        # we convert this to a set to remove possible duplicates as it doesn't affect the sequence count
        nums_set = set(nums)
        longest_sequence: [int] = 0

        for number in nums:
            # we know a sequence starts if it doesn't have its previous number
            if (number - 1) not in nums_set:
                length: [int] = 0
                while (number + length) in nums_set:  # we continue to iterate as long as the sequence grows
                    length += 1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence


print(Solution().longest_consecutive(nums=[2, 20, 4, 10, 3, 4, 5]))  # output = 4
print(Solution().longest_consecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1]))  # output = 7
print(Solution().longest_consecutive(nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # output = 7
