class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        
        histo = [set() for _ in range(len(nums)+1)]
        for i, freq in freqs.items():
            histo[freq].add(i)

        ans = []
        count = k
        for idx in range(len(nums), -1, -1):
            count -= len(histo[idx])
            ans.extend(histo[idx])
            if count == 0:
                return ans
