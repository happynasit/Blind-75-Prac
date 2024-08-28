class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')

        for index in range(len(nums)):
            length = []            
            j = index

            while j < len(nums) and sum(length) < target:
                length.append(nums[j])
                j = j + 1
            
            print(length)
            if sum(length) >= target:
                min_len = min(min_len, len(length))

        if min_len != float('inf'):
            return min_len
        else:
            return 0

