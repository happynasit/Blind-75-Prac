class Solution:
    def countBits(self, n: int) -> List[int]:
        # Result
        bits = []
        for num in range(0, n+1):
            count = 0
            binary_num = str(bin(num)[2:])
            print(binary_num)
            count = binary_num.count("1")
            print(count)
            bits.append(count)
        return bits
