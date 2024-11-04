class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        left_pointer: [int] = 0
        right_pointer: [int] = len(numbers) - 1

        while left_pointer < right_pointer:
            total = numbers[left_pointer] + numbers[right_pointer]

            if total == target:
                return [left_pointer + 1, right_pointer + 1]
            elif total < target:
                left_pointer += 1
            elif total > target:
                right_pointer -= 1


print(Solution().two_sum(numbers=[2, 7, 11, 15], target=9))
print(Solution().two_sum(numbers=[2, 3, 4], target=6))
print(Solution().two_sum(numbers=[-1, 0], target=-1))
