class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_lst = set(nums)
        for value in new_lst:
            if nums.count(value) > (len(nums) // 2):
                return value
