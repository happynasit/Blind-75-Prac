class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = []
        l.extend(nums1)
        l.extend(nums2)
        l.sort()
        if len(l) % 2 != 0:
            index = (len(l) // 2)
            return l[index]
        else:
            index = (len(l) // 2)
            return (l[index] + l[index - 1]) / 2
