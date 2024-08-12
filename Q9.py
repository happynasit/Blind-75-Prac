class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False

        # second method
        # This runs slower, but still just math related so 
        '''
        if x < 0:
            return False
        else:
            reverse = 0
            xcopy = x
            while x > 0:
                reverse = (reverse * 10) + (x % 10)
                x = x // 10
            return reverse == xcopy
        '''
