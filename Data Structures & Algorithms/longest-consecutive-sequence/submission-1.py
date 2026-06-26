class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        lens = {k : 0 for k in set(nums)}

        for num in lens.keys():
            leftlen = lens.get(num - 1, 0)
            rightlen = lens.get(num + 1, 0)
            totallen = leftlen + rightlen + 1

            lens[num-leftlen], lens[num+rightlen], lens[num] = totallen, totallen, totallen
        
            maxlen = max(maxlen, totallen)
        print(lens)
        return maxlen

        
            


