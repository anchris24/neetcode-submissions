class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastpos = {}
        for i, ch in enumerate(s):
            lastpos[ch] = i
        
        end, start = 0, 0
        ans = []
        for i, ch in enumerate(s):
            end = max(end, lastpos[ch])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        
        return ans

        
