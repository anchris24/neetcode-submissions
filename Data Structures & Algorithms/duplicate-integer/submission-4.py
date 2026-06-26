class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashset = []
        for i in nums:
            if i in hashset:
                return True
            hashset.append(i)
        return False