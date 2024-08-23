class Solution:
    def intToRoman(self, num: int) -> str:
        rom_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        rom = ''

        while num != 0:
            max_so_far = min(rom_nums.values())

            for i in rom_nums.values():
                if max_so_far <= i and i <= num:
                    max_so_far = i
            
            print(max_so_far)
           
            rom_max = list(rom_nums.keys())[list(rom_nums.values()).index(max_so_far)]
            rom += rom_max
            num = num - max_so_far

        print(rom)
            
        rom = rom.replace('DCCCC', 'CM')
        rom = rom.replace('CCCC', 'CD')
        rom = rom.replace('LXXXX', 'XC')
        rom = rom.replace('XXXX', 'XL')
        rom = rom.replace('VIIII', 'IX')
        rom = rom.replace('IIII', 'IV')

        print(rom)

        return rom
