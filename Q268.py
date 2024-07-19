class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        list_ = [i for i in range(0, n + 1)]
        remaining = list(set(list_) - set(nums))
        return(remaining[0])
