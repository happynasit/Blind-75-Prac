class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            # the value in the right
            val = nums.pop()
            print(val)
            nums.insert(0, val)
            print(nums)
