class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in mp:
                mp[sorted_string].append(s)
            else:
                mp[sorted_string] = [s]
        return mp.values()
