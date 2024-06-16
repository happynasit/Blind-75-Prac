class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        create each pair and store it as a list
        then for each pair we check their sum and whoever's sum is the target is the
        two sum list
        """
        for i in range(len(nums)):
            # Finding the difference
            diff = target - nums[i]

            list_nums = nums
            list_nums[i] = "_"

            for j in range(len(list_nums)):
                if list_nums[j] == diff:
                    return [i, j]
                
            list_nums[i] = nums[i]

        ## This is similar only except it is a bit faster in runtime
        # for i in range(len(nums)):
        #     # Finding the difference
        #     diff = target - nums[i]

        #     list_nums = nums[:]
        #     list_nums[i] = "_"

        #     if diff in list_nums:
        #         return [i, list_nums.index(diff)]
        #         break
                
        #     list_nums[i] = nums[i]

        
