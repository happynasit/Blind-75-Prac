class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = 1
        # Naive approach
        if n == 0:
            return 0
        else:
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count


        return count
