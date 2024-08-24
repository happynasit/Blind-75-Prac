class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_index = []
        s_index = []
        s_list = s.split()
        for i in pattern:
            pattern_index.append(pattern.index(i))
        for j in s_list:
            s_index.append(s_list.index(j))
            
        return pattern_index == s_index
