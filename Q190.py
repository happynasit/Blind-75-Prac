class Solution:
    def reverseBits(self, n: int) -> int:

      # fill it and make it into hexadecimal type
        str_n = bin(n)[2:].zfill(32)

      # then reverse the bits using the [::-1]
        rev_n = str_n[::-1]
      # Convert it to decimal
        int_number = int(rev_n, 2)
        
        return int_number
