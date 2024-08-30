class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all the non alpha numeric by simply storing the main alpha numeric 
        # in another string. and lower it
        
        ss = ''
        for i in s:
            if i.isalnum():
                ss = ss + i.lower()
       
        # now to check whether or not it is a pallindrome
        return ss == ss[len(ss) :: -1]
        
                
        
        
