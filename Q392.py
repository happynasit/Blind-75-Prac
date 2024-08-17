class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = len(t) - 1
        s_copy = s
        add = ""
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s_copy[j]:
                s_copy.replace(t[i], '')
                add += t[i]
                j += 1
            i = i + 1
          
        return add == s
