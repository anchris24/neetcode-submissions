class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ids = [0] * 26
        schedule = []
        heapq.heapify(schedule)

        for i in tasks:
            curr = ord(i) - ord("A")
            heapq.heappush(schedule, ids[curr])
            ids[curr] += n + 1
        

        num = 0
        while schedule:
            curr = heapq.heappop(schedule) + 1
            if num >= curr:
                num += 1
            else:
                num = curr
        
        return num