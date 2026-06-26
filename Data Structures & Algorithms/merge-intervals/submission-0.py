class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        start, end = intervals[0]
        for i in intervals:
            a, b = i
            if a <= end:
                end = max(b, end)
            else:
                ans.append([start, end])
                start, end = a, b
        ans.append([start, end])
        return ans