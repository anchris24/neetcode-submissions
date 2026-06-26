class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        leftmax, rightmax = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < leftmax:
                    water += leftmax-height[left]
                else:
                    leftmax = height[left]
                left += 1
            else:
                if height[right] < rightmax:
                    water += rightmax-height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return water