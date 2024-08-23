class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        main_word = strs[0]
        min_length = min([len(word) for word in strs])
        for index in range(min_length):
            if not all([main_word[index] == word[index] for word in strs]):
                break
            prefix += main_word[index]

        # Common Prefix 
        return prefix
        
