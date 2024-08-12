class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = 0
        for i in digits:
            val = val * 10 + i
        
        val += 1
        plus_one = []
        for i in str(val):
            plus_one.append(int(i))

        return plus_one
