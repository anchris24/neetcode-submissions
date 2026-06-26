class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                out[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            stack.append( (idx, val) )
        return out
            