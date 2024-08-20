class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # initializing and counting the FIRST TWO ELEMENTS
        index = 0
        dict_a = {}

        for i in range(len(nums)):
            dict_a[nums[i]] = dict_a.get(nums[i], 0) + 1

            if dict_a[nums[i]] <= 2:
                nums[index] = nums[i]
                index += 1
            print(nums)

        return index
