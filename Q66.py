class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        val = 0
        for i in digits:
            val = val * 10 + i
        
        val += 1
        plus_one = []
        for i in str(val):
            plus_one.append(int(i))
        return plus_one
        """
        # THIS IS WITHOUT USING PLUS SIGN, I USED A CARRY (LIKE BINARY) TO KEEP CHECKING ON THE NUMBERS WHETHER THEY ARE NINE OR NOT
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
        else:
            carry = 1
            i = len(digits) - 1
            while i >= 0:
                if carry + digits[i] == 10:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += carry
                    carry = 0
                i = i - 1
            print(digits)
            if carry == 1:
                digits.insert(0, 1)
        return digits
