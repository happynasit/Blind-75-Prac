class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # val_ = all(val < 0 for val in nums)
        # print(val_)
        # if len(nums) == 1:
        #     return nums[0]
        # elif val_ is True:
        #     return max(nums)
        # else:
        #     # The max sum so far will be the sum of the entire array
        #     left = 0
        #     right = len(nums)
        #     max_sum = sum(nums)
        #     while left <= right:
        #         if nums[left] < nums[right-1]:
        #             left = left + 1
        #             max_sum = max(max_sum, sum(nums[left:right]))
        #         elif nums[left] > nums[right-1]:
        #             right = right - 1
        #             max_sum = max(max_sum, sum(nums[left:right]))
        #         else:
        #             right = right - 1
                    
        # return max_sum
        maxSum = float('-inf')
        currentSum = 0
    
        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum
