### LeetCode 75 - Q6

class Solution:
    def reverseWords(self, s: str) -> str:
        ## Split the string (default by whitespace) into words and put into an array
        ## Then reverse this array
        original = s.split()
        reverse = original[::-1]

        ## Append spaces to each of the words (except the last one) and create reversed string
        for word in range(len(reverse) -1):
            reverse[word] += ' '
        return ''.join(reverse)