class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]].append(i)
            else:
                s_dict[s[i]] = [i]
        
        for j in range(len(t)):
            if t[j] in t_dict:
                t_dict[t[j]].append(j)
            else:
                t_dict[t[j]] = [j]
        for locations in s_dict.values():
            if locations not in t_dict.values():
                return False
        return True
        """
        ss = []
        tt = []

        for i in s:
            ss.append(s.index(i))

        for j in t:
            tt.append(t.index(j))

        return ss == tt  
