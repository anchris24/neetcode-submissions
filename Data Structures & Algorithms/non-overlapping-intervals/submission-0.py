class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        countremove = 0
        intervals.sort(key=lambda i:i[0])
        end = intervals[0][0] - 1
        for i in intervals:
            a, b = i
            if a >= end:
                end = b
            else:
                countremove += 1
                end = min(end, b)
        return countremove
