### LeetCode 75 - Q5

class Solution:
    def reverseVowels(self, s: str) -> str:
        ## The goal is to have two pointers on the left and right respectively (of the string)
        ## Moving towards eachother until they meet in the middle, reversing vowel places as they go
        
        ## Make a vowel set to check against
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

        ## Strings are immutable in python, so convert to a list
        s = list(s)
        left, right = 0, len(s) - 1

        ## Switch vowels, keep other characters in their place
        while (left < right):
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        ## Once completed, convert back to string and return
        return ''.join(s)