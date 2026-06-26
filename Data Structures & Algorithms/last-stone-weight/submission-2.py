class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones2 = [-1 * stone for stone in stones]
        heapq.heapify(stones2)

        while len(stones2) > 1:
            print(stones2)
            a, b = heapq.heappop(stones2), heapq.heappop(stones2)
            if a < b:
                heapq.heappush(stones2, a - b)
        
        if not stones2:
            return 0
        return -stones2[0]