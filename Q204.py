class Solution:
    def countPrimes(self, n: int) -> int:
        """
        nums_till_n = 0
        
        i = 0
        if n == 0 or n == 1:
            nums_till_n = 0
        else:
            while i < n:
                count = 0
                for j in range(1, i + 1):
                    if i % j == 0 :
                        count = count + 1
                if count == 2:
                    nums_till_n = nums_till_n + 1
                i = i + 1
                    
        return nums_till_n
        """

        if n<=2:
            return 0
        ref=[True]*(n)
        i=2
        while (i*i)<n:
            if ref[i]:
                for j in range(i*i,n,i):
                    ref[j]=False
            i+=1
        return ref.count(True)-2
