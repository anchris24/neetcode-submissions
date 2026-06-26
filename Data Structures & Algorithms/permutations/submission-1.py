class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []
        used = [False] * len(nums)

        def backtrack(templist):
            if len(templist) == len(nums):
                perms.append(templist[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                templist.append(nums[i])

                backtrack(templist)
                templist.pop()
                used[i] = False

        backtrack([])
        return perms