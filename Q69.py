class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            return 0
        elif x==1:
            return 1
        else:
            for i in range(1,x+1):
                if i*i > x:
                    return i-1
        """
        if x==0:
            return 0
        elif x==1:
            return 1
        else:
            left = 0
            right = x
            while left <= right:
                mid = (left + right) // 2
                if mid * mid < x:
                    left = mid + 1
                elif mid * mid > x:
                    right = mid - 1
                else:
                    return mid
            return right
        """
