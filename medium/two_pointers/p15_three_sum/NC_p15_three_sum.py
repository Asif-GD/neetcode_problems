class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets_list: list[list[int]] = list()

        for index, first_number in enumerate(nums):
            if index > 0 and first_number == nums[index - 1]:
                continue
            else:
                left_pointer: [int] = index + 1
                right_pointer: [int] = len(nums) - 1

                while left_pointer < right_pointer:
                    three_sum: [int] = first_number + nums[left_pointer] + nums[right_pointer]
                    if three_sum > 0:
                        right_pointer -= 1
                    elif three_sum < 0:
                        left_pointer += 1
                    else:
                        triplets_list.append([first_number, nums[left_pointer], nums[right_pointer]])
                        # a tricky condition [-2, -2, 0, 0, 2, 2]
                        left_pointer += 1
                        while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                            left_pointer += 1

        return triplets_list


# print(Solution().three_sum(nums=[-4, -1, -1, 0, 1, 2]))
print(Solution().three_sum(nums=[-1, 0, 1, 2, -1, -4]))
