## LeetCode 75 - Q4

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        ## Check if any flowers need planting to begin with
        if n == 0:
            return True

        ## Then for each flower in the array, checking whether it is a boundary flower and it's availability for planting or whether the two plots adjacent to it don't contain flowers
        for i in range(len(flowerbed)):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                ## If the number of flowers needed to be planted reaches 0 before iterations finish, the output becomes True
                n-=1
                flowerbed[i] = 1
                if n == 0: 
                    return True
        return False