class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = dict()

        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1

        for i in nums_dict:
            if nums_dict[i] == 1:
                return i
