class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []

        def backtrack(avail, templist):
            if len(templist) == len(nums):
                perms.append(templist)
                return
            
            for i in range(len(avail)):
                curr = avail[i]
                rest = avail[:i] + avail[i+1:]

                backtrack(rest, [curr] + templist)
        backtrack(nums, [])
        return perms