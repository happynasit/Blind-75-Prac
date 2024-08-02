class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            # The max sum so far will be the sum of the entire array
            left = 0
            right = len(nums)
            max_sum = sum(nums)
            while left < right:
                if nums[left] < nums[right-1]:
                    left = left + 1
                    max_sum = max(max_sum, sum(nums[left:right]))
                elif nums[left] > nums[right-1]:
                    right = right - 1
                    max_sum = max(max_sum, sum(nums[left:right]))
                else:
                    right = right - 1
                    max_sum = max(max_sum, sum(nums[left:right]))

        return max_sum
