class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # len_ = k % len(nums)
        # for _ in range(len_):
        #     # the value in the right
        #     val = nums.pop()
        #     print(val)
        #     nums.insert(0, val)
        #     print(nums)

        if k == 0:
            return

        size = len(nums)

        # this is in case some elements don't really need a rotation
        k = k if k <= size else k % size
        nums[k:], nums[:k] = nums[:size - k], nums[size - k:]
