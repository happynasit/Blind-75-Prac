class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # this is for the nums 2 part, we will replace it from
        for i in range(n):
            nums1[len(nums1) - i - 1] = nums2[i]

        nums1.sort()

       
        
