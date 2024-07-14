class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = nums.sort()
        result = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < 0:
                    left +=1
                elif total > 0:
                    right -=1
                else:
                    triplet = [nums[left], nums[right], nums[i]]
                    result.append(triplet)
                    while left < right and nums[left] == triplet[0]:
                        left += 1
                    while left < right and nums[right] == triplet[1]:
                        right -= 1
        return result
