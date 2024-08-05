class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # return max product of a subarray
        
        maxSum = float('-inf')
        currentSum = 1
        
        for num in nums:
            currentSum *= num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 1
        
        return maxSum
