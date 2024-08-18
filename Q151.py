class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()

        result = ''

        for i in s_list[::-1]:
            result += i
            result += " "
        
        return result[:len(result)-1]
