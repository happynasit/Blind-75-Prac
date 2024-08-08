class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)

        print(decimal_a)
        print(decimal_b)

        sum_ = decimal_a + decimal_b

        return str(bin(sum_)[2:])
