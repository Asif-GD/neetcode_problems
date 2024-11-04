class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:

        index_list: list[int] = []
        for index, number in enumerate(numbers):
            # print(f"i,n: {index, number}")
            second_number = target - number
            # print(f"second_number: {second_number}")
            if second_number in numbers:
                # print("inside if")
                index_list.append(index + 1)
                second_index = numbers.index(second_number, index + 1)
                index_list.append(second_index + 1)
                return index_list


print(Solution().two_sum(numbers=[2, 7, 11, 15], target=9))
print(Solution().two_sum(numbers=[2,3,4], target=6))
print(Solution().two_sum(numbers=[-1,0], target=-1))
