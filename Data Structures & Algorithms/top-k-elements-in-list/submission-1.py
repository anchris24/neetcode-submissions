class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        counts = [[] for _ in range(len(nums)+1)]
        for num, cnt in freq.items():
            counts[cnt].append(num)
        print(counts)
        
        ans = []
        for i in range(len(nums), -1, -1):
            ans.extend(counts[i])
            if len(ans) == k:
                return ans