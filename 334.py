### LeetCode 75 - Q8

class Solution:
    def increasingTriplet(self, nums):
        ## Initially set two values of infinity. This means that regardless of the presented numbers the loop will precede without triggering true.
        min1 = float('inf')
        min2 = float('inf')

        ## The loop will find the smallest value in the loop and set it to min1 (if triplet not found prior)
        ## Likewise for min2 with the second smallest integer
        ## A larger number then both will prove triplet that meets criteria, a smaller value than min1
        ## Will set a new min1 and then a value between min1 and min2 will set min2's new value
        ## If true is not triggered by the end of iterations, it indicates there is no triplet that meets the criteria and false will be returned
        for n in nums:
            if n <= min1:
                min1 = n 
            elif n <= min2:
                min2 = n  
            else:
                return True 
        return False 