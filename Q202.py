class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 4:
            n = sum([int(value)**2 for value in str(n)])
        if n == 1:
            return True
        else:
            return False
