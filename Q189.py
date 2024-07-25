class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        removing_elements = len(nums) - k # the index that we should start with
        
        to_append = nums[0: removing_elements]
        
        nums = nums[removing_elements: len(nums)]
        nums.extend(to_append)
        print(nums)
