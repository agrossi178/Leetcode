### LeetCode 75 - Q7

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ## This solution utilises prefix and suffix of the current index. The index's output is calculated by multipling the product of the previous integers by the product of the following integers.
        
        output = []
        prefix, suffix = 1, 1

        ## First loop calculates all prefixes and stores them in the output array (O(1) in space complexity excluding the output array)
        for i in range(len(nums)):
            output.append(nums[i] * prefix)
            prefix = nums[i] * prefix
        
        ## Next loop calculates the suffixes, and the output array using previously calculated prefixes
        for i in range(len(nums)):
            if i == len(nums)-1:
                prefix = 1
            else:
                prefix = output[len(nums)-i-2]
            if i == 0:
                suffix = 1
            else:
                suffix = suffix * nums[(len(nums)-i)]

            output[len(nums)-i-1] = prefix * suffix
            
        return output