class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # bin() returns a binary version of a value
        for i in str(bin(n)):
            if i == '1':
                count = count + 1
        return count
