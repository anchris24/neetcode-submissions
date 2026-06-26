"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        
        sidx, eidx = 0, 0
        count = 0
        ans = 0
        while sidx < len(intervals):
            if start[sidx] < end[eidx]:
                count += 1
                sidx += 1
            else:
                eidx += 1
                count -= 1
            ans = max(ans, count)
        
        return ans

