class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            double = numbers[left] + numbers[right]
            if double == target:
                return [left + 1, right + 1]
                break
            elif double < target:
                # that means that we need to increase the total
                left += 1
            else:
                # that means we need to decrease the total
                right -= 1
            
       
