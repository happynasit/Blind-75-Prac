class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict_nums = dict()

        for i in nums:
            if i in dict_nums:
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1
        
        for i in dict_nums:
            if dict_nums[i] == 1:
                return i
