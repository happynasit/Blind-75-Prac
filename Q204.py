class Solution:
    def countPrimes(self, n: int) -> int:
        nums_till_n = 0
        
        i = 0
        while i < n:
            count = 0
            for j in range(1, i + 1):
                if i % j == 0 :
                    count = count + 1
            if count == 2:
                nums_till_n = nums_till_n + 1
            i = i + 1
                    
        return nums_till_n
