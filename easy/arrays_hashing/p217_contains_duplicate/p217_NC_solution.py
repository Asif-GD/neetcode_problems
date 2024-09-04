def contains_duplicate(self, nums: list[int]) -> bool:
    # if the list contains 1 item or lesser:
    if len(nums) <= 1:
        return False

    hashset = set()
    for number in nums:
        if number in hashset:
            return True

        hashset.add(number)

    return False
