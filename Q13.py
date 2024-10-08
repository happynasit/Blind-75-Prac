class Solution:
    def romanToInt(self, s: str) -> int:

        # This is simply converting the Ones that are before the main number
        # thqt is IX is before X, to VIIII so that it gets easily added up.
        rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        #less_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        int_value = 0
        
        i = 0
        s = s.replace('IV', 'IIII')
        s = s.replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC')
        s = s.replace('CM', 'DCCCC')

        for i in s:
            int_value += rom_dict[i]
            
        
        return int_value
