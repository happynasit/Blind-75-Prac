class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do NOT return anything, MODIFY nums in-place instead.
        Same type of question asked in one of the interviews except it was real colours instead of integers 0, 1 and 2.
        """
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        print(zero)
        print(one)
        print(two)
        
        for i in range(0, zero):
            nums[i] = 0
        for j in range(zero, zero + one):
            nums[j] = 1
        for k in range(zero + one, len(nums)):
            nums[k] = 2
        
