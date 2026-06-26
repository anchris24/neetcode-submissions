class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        powerset = []
        curr = nums[0]
        rest = nums[1:]

        restsubsets = self.subsets(rest)
        for subset in restsubsets:
            powerset.append(subset)
            powerset.append([curr] + subset)

        return powerset