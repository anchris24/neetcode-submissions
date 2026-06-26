class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        schedule = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            schedule.append(intervals[idx])
            idx += 1
        
        if idx < len(intervals) and intervals[idx][0] < newInterval[0]:
            newInterval[0] = intervals[idx][0]
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        
        
        schedule.append(newInterval)
        while idx < len(intervals):
            schedule.append(intervals[idx])
            idx += 1
        return schedule