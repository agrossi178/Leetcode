## LeetCode 75 - Q1

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ## Initialise merged word, determine length of longest string
        word = ""
        if len(word2) > len(word1):
            length = len(word2)
        else:
            length = len(word1)

        ## Use longest string length to determine iteration length, alternately append characters
        for i in range(length):
            if i < len(word1):
                word += word1[i]
            if i < len(word2):
                word += word2[i]
        return word