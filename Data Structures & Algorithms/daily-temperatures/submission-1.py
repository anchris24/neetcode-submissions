class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        out = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, _ = stack.pop()
                out[i] = idx - i
            stack.append( (idx, temp) )
        return out