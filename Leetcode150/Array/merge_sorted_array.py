class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        first one is simple n + mlogm runtime

        second one is more optimised, here we start with comparing the larges value between the two lists and go from right to left.
        """
        # using the sort method : runtime thats used is n + mlogm
        # for i in range(n):
        #     nums1[len(nums1) - i - 1] = nums2[i]
        # nums1.sort()



        
        # using the O(m + n)
        # last index of nums1
        i = m + n - 1
        m = m-1
        n = n-1
        while m >= 0 and n >= 0:
            if nums2[n] < nums1[m]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
           
            i-=1
       
        while n >= 0:
            nums1[i] = nums2[n]
            n, i = n-1, i-1
       
