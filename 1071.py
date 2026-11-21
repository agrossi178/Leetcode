## LeetCode 75 - Q2

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        ## Check character structures are the same
        if str1 + str2 != str2 + str1:
            return ""

        ## Divide len1 by len2 to identify remainder. Repeat process until remainder = 0
        else:
            while len2:
                len1, len2 = len2, len1 % len2
            return str1[:len1]