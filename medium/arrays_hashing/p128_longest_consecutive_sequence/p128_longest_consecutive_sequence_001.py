class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:

        # edge-case 1: when nums is empty
        if len(nums) == 0:
            return 0

        nums.sort()
        # print(f"nums: {nums}")
        count: [int] = 1
        count_list: [list[int]] = list()

        for index in range(len(nums)):
            # print("inside for")
            # print(f"index: {index}")
            if index == len(nums) - 1:
                break
            else:
                # when two numbers are same, it doesn't affect the sequence count.
                if (nums[index + 1] - nums[index]) == 1:
                    count += 1
                # when the sequence breaks; it's recorded to the count_list, count is reset to 1
                elif (nums[index + 1] - nums[index]) > 1:
                    count_list.append(count)
                    count = 1

        count_list.append(count)
        return max(count_list)


print(Solution().longest_consecutive(nums=[2, 20, 4, 10, 3, 4, 5]))  # output = 4
print(Solution().longest_consecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1]))  # output = 7
print(Solution().longest_consecutive(nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # output = 7
