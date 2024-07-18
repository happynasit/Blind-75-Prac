class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as a while loop and single value check 
        while (b & mask) > 0:
            #carry basically returns the positions that might have a carry, which is shifted left
            carry = ( a & b ) << 1
            #we add without having carry using xor
            a = (a ^ b) 
            #then we make the b as carry and repeat the loop so the sum is added to carry
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
