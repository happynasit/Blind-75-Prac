class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dict_ransomnote = {}
        # dict_magazine = {}

        # for letter in ransomNote:
        #     dict_ransomnote[letter] = dict_ransomnote.get(letter, 0) + 1

        # for second in magazine:
        #     dict_magazine[second] = dict_magazine.get(second, 0) + 1

        # so_far = True
        # for characters in dict_ransomnote:
        #     if characters not in dict_magazine or dict_ransomnote[characters] > dict_magazine[characters]:
        #         so_far = False
        # return so_far

        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
