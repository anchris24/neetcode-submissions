"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for i in intervals:
            events.append( (i.end, -1) )
            events.append( (i.start, 1) )
        
        heapq.heapify(events)

        ans, count = 0, 0
        while events:
            _, add = heapq.heappop(events)
            count += add

            ans = max(ans, count)
        
        return ans


