class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        id = 0
        k = len(nums)
        while id < len(nums):
            if nums[id] == val:
                k -= 1
                nums.pop(id)
            
            else:
                id += 1
        
        return k