class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxarea = 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxarea = max(maxarea, area)
            print(left, right, maxarea)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
            
        
        return maxarea

