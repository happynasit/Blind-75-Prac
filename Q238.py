class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        print(product)
        while i < len(nums):
            res = product//nums[i]
            print(res)
            answer.append(res)
            i = i + 1
        return answer
