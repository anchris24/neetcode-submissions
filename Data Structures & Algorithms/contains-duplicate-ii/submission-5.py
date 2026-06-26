class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        window = set()
        for i in range(k):
            if i  == len(nums):
                return False

            if nums[i] in window:
                return True

            window.add(nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] in window:
                return True
            window.remove(nums[i-k])
            window.add(nums[i])

        return False