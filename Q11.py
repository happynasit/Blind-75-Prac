class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        i = 0
        max_area = 0

        while i < len(height):
            # take the minimum of left and right, which will be the main height
            min_height = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, width * min_height)

            if height[left] < height[right]:
                left = left + 1
            elif height[right] > height[left]:
                right = right - 1
            else:
                right = right - 1 
            i = i + 1
        return max_area
