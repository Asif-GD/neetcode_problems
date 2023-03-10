"""
algorithm:
- if previous and next are zero, replace 0(empty) with 1(flower)
- when n flowers are planted, return True
- else return False
"""


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    new_flowerbed = [0] + flowerbed + [0]
    index = 1
    while n > 0 and index < len(new_flowerbed) - 1:
        if new_flowerbed[index] == 0:
            if new_flowerbed[index - 1] == 0 and new_flowerbed[index + 1] == 0:
                new_flowerbed[index] = 1
                n -= 1
                if n == 0:
                    return True
        index += 1
    return True if n == 0 else False


print(can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(can_place_flowers(flowerbed=[0, 0, 1, 0, 1], n=1))
print(can_place_flowers(flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2))
print(can_place_flowers(flowerbed=[0, 0, 0], n=2))
print(can_place_flowers(flowerbed=[1, 0, 1, 0, 1, 0, 1], n=0))
