### LeetCode 75 - Q3

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ## Initialise the greatest integer in candies array and output array
        greatest = 0
        output = []

        ## Iterate through array to determine the greatest integer, store it
        for i in candies:
            if greatest < i:
                greatest = i
        
        # Compare greatest integer to each kid with extra candies, add boolean to output array
        for j in candies:
            if (j + extraCandies) >= greatest:
                output.append(True)
            else:
                output.append(False)
        return output