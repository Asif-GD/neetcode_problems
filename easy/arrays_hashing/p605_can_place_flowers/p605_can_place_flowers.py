"""
algorithm:
if there are 2n + 1 continuous 0s in the flowerbed, n flowers can be placed.
"""


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    new_flowerbed = [0] + flowerbed + [0, 1]
    empty_flowerbed = 0
    can_plant_flowers = 0
    for bit in new_flowerbed:
        if bit == 1:
            if empty_flowerbed > 3:
                if empty_flowerbed % 2 == 0:
                    empty_flowerbed -= 1
                can_plant_flowers += int((empty_flowerbed - 1) / 2)
            elif empty_flowerbed == 3:
                can_plant_flowers += int((empty_flowerbed - 1) / 2)
            empty_flowerbed = 0
            if can_plant_flowers >= n:
                return True
        else:
            empty_flowerbed += 1

    return not bool(n - can_plant_flowers)


print(can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(can_place_flowers(flowerbed=[0, 0, 1, 0, 1], n=1))
print(can_place_flowers(flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2))
print(can_place_flowers(flowerbed=[0, 0, 0], n=2))
