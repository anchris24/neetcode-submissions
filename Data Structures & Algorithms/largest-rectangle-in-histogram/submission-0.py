class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        idstack = []
        heights.append(0)
        maxarea = 0

        for idx, height in enumerate(heights):
            while idstack and heights[idstack[-1]] > height:
                startid = idstack.pop()
                width = idx
                if idstack:
                    width = idx - idstack[-1] - 1

                area = heights[startid] * width
                maxarea = max(maxarea, area)
            idstack.append(idx)
        
        return maxarea