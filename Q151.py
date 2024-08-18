class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''

        for i in s.split()[::-1]:
            result += i
            result += " "
        
        return result[:len(result)-1]
