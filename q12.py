class Solution:
    def intToRoman(self, num: int) -> str:
        
        rom_nums = {1: "I",5: "V",4: "IV",10: "X",9: "IX",50: "L",40: "XL",100: "C",90: "XC",500: "D",400: "CD",1000: "M", 900: "CM"}
        rom = ''

        while num != 0:
            max_so_far = min(rom_nums.keys())

            for i in rom_nums.keys():
                if max_so_far <= i and i <= num:
                    max_so_far = i
            
            rom += rom_nums[max_so_far]
            num = num - max_so_far

        print(rom)

        return rom
